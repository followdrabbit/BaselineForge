import streamlit as st
from datetime import datetime
from pathlib import Path
from typing import List, Tuple
from modules.config_loader import ConfigLoader
from modules.url_processor import URLProcessor
from modules.id_generator import IDGenerator
from modules.openai_service import OpenAIService
from modules.html_generator import HTMLGenerator
from modules.cleanup_util import cleanup_generated_files
from modules.agent_processor import AgentProcessor
from modules.data_importer import load_markdown_as_dataframe

def initialize_dependencies(selected_language: str) -> Tuple[ConfigLoader, URLProcessor, HTMLGenerator, dict, Path, str]:
    """
    Inicializa as dependências da aplicação garantindo que apenas UM session_id seja gerado
    por sessão. O session_id é encurtado para evitar ultrapassar limites de path no Windows.
    """
    config_loader = ConfigLoader(config_file="config/config.json")
    try:
        menu_config = config_loader.get_menu(selected_language)
    except Exception as e:
        st.error(f"Erro ao carregar as configurações do idioma {selected_language}: {e}")
        st.stop()

    if "session_id" not in st.session_state:
        st.session_state.session_id = IDGenerator.generate_uuid()

    session_id = st.session_state.session_id
    short_session_id = session_id[:8]
    base_session_dir = Path("artefacts") / f"s_{short_session_id}"
    base_session_dir.mkdir(parents=True, exist_ok=True)
    url_processor = URLProcessor(str(base_session_dir), short_session_id)
    html_generator = HTMLGenerator()

    return config_loader, url_processor, html_generator, menu_config, base_session_dir, short_session_id


def get_user_inputs(menu_config: dict) -> Tuple[str, str, List[str], str]:
    """
    Coleta os inputs do usuário (fornecedor, tecnologia, URLs e setor) usando o menu de configuração.
    """
    vendor = st.selectbox(
        menu_config.get("select_vendor", "Selecione o Fornecedor"),
        ["AWS", "Azure", "GCP", "Huawei", "OCI"]
    )
    tecnologia = st.text_input(
        menu_config.get("enter_technology_name", "Digite o nome da Tecnologia")
    )
    urls_input = st.text_area(
        menu_config.get("enter_urls", "Digite até 10 URLs separadas por vírgula"), ""
    )
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    
    # Novo campo para selecionar o setor
    setor = st.selectbox(
        "Selecione o setor de risco a ser avaliado:",
        ["Bancário", "Farmacêutico", "Energético", "Automotivo", "Varejo", "Manufatura"]
    )
    
    return vendor, tecnologia, urls, setor


def generate_baseline_html(
    html_generator: HTMLGenerator,
    config_loader: ConfigLoader,
    selected_language: str,
    final_markdown_path: str,
    artifacts_dir: Path,
    run_short_id: str,
    id_unico: str
) -> str:
    """
    Gera o HTML final do baseline usando o HTMLGenerator.
    O run_short_id é usado para nomear o arquivo de saída e o id_unico é passado
    para manter o padrão do ID na tabela de SECURITY CONTROLS.
    """
    template_path = "templates/template_html.html"
    output_html_path = artifacts_dir / f"r_{run_short_id}_final.html"

    html_sections = config_loader.get_html_sections(selected_language)
    version_info = config_loader.get_version_info(selected_language)
    history_table = config_loader.get_history_table(selected_language)
    control_table_labels = config_loader.get_control_table(selected_language)

    html_content = html_generator.generate_html(
        template_path=template_path,
        output_html=str(output_html_path),
        html_sections=html_sections,
        version_info=version_info,
        controls_df=load_markdown_as_dataframe(final_markdown_path.replace("final.md", "controlgen_unificado_ControlRefiner.md")),
        risks_df=load_markdown_as_dataframe(final_markdown_path.replace("final.md", "controlgen_unificado_RiskEvaluator.md")),
        history_config=history_table,
        base_control_id=id_unico
    )

    return html_content


def run_pipeline(
    config_loader: ConfigLoader,
    url_processor: URLProcessor,
    html_generator: HTMLGenerator,
    menu_config: dict,
    base_session_dir: Path,
    selected_language: str,
    short_session_id: str
) -> Tuple[List[str], Path, str]:
    """
    Executa todo o pipeline para gerar o baseline.
    A cada clique em "Gerar Baseline", cria um subdiretório usando run_id.
    Retorna a lista de arquivos gerados, o diretório de artefatos e o id_unico.
    """
    vendor, tecnologia, urls, setor = get_user_inputs(menu_config)
    with st.form("Formulário de ID"):
        submit_button = st.form_submit_button(menu_config.get("generate_baseline", "Gerar Baseline"))
    if not submit_button:
        st.info("Aguardando submissão do formulário...")
        return [], base_session_dir, ""
    if not (vendor and tecnologia and urls):
        st.error("Por favor, preencha todos os campos obrigatórios.")
        return [], base_session_dir, ""
    if len(urls) > 10:
        st.error("Por favor, insira no máximo 10 URLs.")
        return [], base_session_dir, ""

    id_unico = IDGenerator.generate_control_id(vendor, tecnologia, datetime.now().year, 1)

    run_id = IDGenerator.generate_uuid()
    run_short_id = run_id[:8]

    run_artifacts_dir = base_session_dir / f"r_{run_short_id}_{id_unico}"
    run_artifacts_dir.mkdir(parents=True, exist_ok=True)

    assistant_id = OpenAIService.initialize_assistant("config/config.json", selected_language, vendor, setor)

    run_url_processor = URLProcessor(str(run_artifacts_dir), run_short_id)

    markdown_files = []
    for url in urls:
        html_content = run_url_processor.fetch_page_content(url)
        if html_content:
            markdown_path = run_url_processor.save_as_markdown(url, html_content)
            markdown_files.append(Path(markdown_path))
        else:
            st.warning(f"Falha ao processar URL: {url}")

    if not markdown_files:
        st.error("Nenhum arquivo Markdown foi gerado. Verifique as URLs fornecidas.")
        return [], run_artifacts_dir, id_unico

    agent_processor = AgentProcessor(config_loader, selected_language, vendor, run_artifacts_dir)
    final_content = agent_processor.process_files(markdown_files)

    final_markdown_path = run_artifacts_dir / f"r_{run_short_id}_final.md"
    final_markdown_path.write_text(final_content, encoding="utf-8")
    prompt_text = ""
    for md_file in run_artifacts_dir.glob("*.md"):
        if "final" not in md_file.name:
            prompt_text += md_file.read_text(encoding="utf-8")
    
    prompt_tokens = OpenAIService.count_tokens(prompt_text, "gpt-4o")
    completion_tokens = OpenAIService.count_tokens(final_content, "gpt-4o")
    token_info = OpenAIService.calculate_cost(prompt_tokens, completion_tokens, model="gpt-4o")

    st.session_state.token_info = token_info
    st.info(f"Tokens do Prompt: {token_info['prompt_tokens']} | Tokens da Resposta: {token_info['completion_tokens']} | Custo Total: US$ {token_info['total_cost']:.4f}")

    return [str(final_markdown_path)], run_artifacts_dir, id_unico


def main():
    st.title("BaselineForge")
    st.markdown("**Confira o repositório do projeto no GitHub:** [BaselineForge](https://github.com/followdrabbit/BaselineForge)")  

    selected_language = st.selectbox(
        "Selecione o idioma desejado | Select the desired language | Seleccione el idioma deseado:",
        ["EN-US", "PT-BR", "ES-ES"]
    )

    config_loader, url_processor, html_generator, menu_config, base_session_dir, short_session_id = initialize_dependencies(selected_language)

    generated_files, artifacts_dir, id_unico = run_pipeline(
        config_loader,
        url_processor,
        html_generator,
        menu_config,
        base_session_dir,
        selected_language,
        short_session_id
    )

    control_refiner_path = artifacts_dir / "controlgen_unified_ControlRefiner.md"
    risk_evaluator_path = artifacts_dir / "controlgen_unified_RiskEvaluator.md"
    if control_refiner_path.exists() and risk_evaluator_path.exists():
        df_controls = load_markdown_as_dataframe(str(control_refiner_path))
        df_risks = load_markdown_as_dataframe(str(risk_evaluator_path))

        html_content = html_generator.generate_html(
            template_path="templates/template_html.html",
            output_html=str(artifacts_dir / f"{id_unico}_final.html"),
            html_sections=config_loader.get_html_sections(selected_language),
            version_info=config_loader.get_version_info(selected_language),
            controls_df=df_controls,
            risks_df=df_risks,
            history_config=config_loader.get("history_table", {}),
            base_control_id=id_unico
        )
        st.download_button(
            label="Download Web Page",
            data=html_content,
            file_name=f"{id_unico}_controls.html",
            mime="text/html"
        )
    else:
        st.warning("Arquivos de controles e riscos não foram encontrados.")

    return generated_files, artifacts_dir

if __name__ == "__main__":
    generated_files = []
    artifacts_dir = ""
    try:
        result = main()
        if result is not None:
            generated_files, artifacts_dir = result
    finally:
        pass
