import streamlit as st
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

# Módulos do projeto
from modules.config_loader import ConfigLoader
from modules.url_processor import URLProcessor
from modules.id_generator import IDGenerator
from modules.openai_service import OpenAIService
from modules.html_generator import HTMLGenerator
from modules.cleanup_util import cleanup_generated_files
from modules.agent_processor import AgentProcessor


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

    # Gera apenas uma vez por sessão do Streamlit
    if "session_id" not in st.session_state:
        st.session_state.session_id = IDGenerator.generate_uuid()

    session_id = st.session_state.session_id
    short_session_id = session_id[:8]  # Reduz o ID para evitar caminhos muito grandes

    # Diretório base da sessão
    base_session_dir = Path("artefacts") / f"s_{short_session_id}"
    base_session_dir.mkdir(parents=True, exist_ok=True)

    # Instancia o URLProcessor, mas note que ele não vai usar session_id no nome dos arquivos
    url_processor = URLProcessor(str(base_session_dir), short_session_id)
    html_generator = HTMLGenerator()

    return config_loader, url_processor, html_generator, menu_config, base_session_dir, short_session_id


def get_user_inputs(menu_config: dict) -> Tuple[str, str, List[str]]:
    """
    Coleta os inputs do usuário (fornecedor, tecnologia e URLs) usando o menu de configuração.
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
    return vendor, tecnologia, urls


def generate_baseline_html(
    html_generator: HTMLGenerator,
    config_loader: ConfigLoader,
    selected_language: str,
    final_markdown_path: str,
    artifacts_dir: Path,
    run_short_id: str
) -> str:
    """
    Gera o HTML final do baseline usando o HTMLGenerator.
    O run_short_id é usado somente para nomear o arquivo de saída .html (opcional).
    """
    template_path = "templates/template_html.html"
    output_html_path = artifacts_dir / f"r_{run_short_id}_final.html"

    html_sections = config_loader.get_html_sections(selected_language)
    version_info = config_loader.get_version_info(selected_language)
    history_table = config_loader.get_history_table(selected_language)
    control_table_labels = config_loader.get_control_table(selected_language)

    html_content = html_generator.generate_html(
        template_path=template_path,
        content_path=final_markdown_path,
        output_html=str(output_html_path),
        html_sections=html_sections,
        history_table=history_table,
        control_table_labels=control_table_labels,
        version_info=version_info
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
) -> Tuple[List[str], Path]:
    """
    Executa todo o pipeline para gerar o baseline. A cada clique em "Gerar Baseline",
    cria um subdiretório usando run_id. Esse run_id não compõe o nome dos arquivos .md,
    mas apenas o nome da pasta.
    """
    vendor, tecnologia, urls = get_user_inputs(menu_config)

    with st.form("Formulário de ID"):
        submit_button = st.form_submit_button(menu_config.get("generate_baseline", "Gerar Baseline"))

    if not submit_button:
        st.info("Aguardando submissão do formulário...")
        return [], base_session_dir

    if not (vendor and tecnologia and urls):
        st.error("Por favor, preencha todos os campos obrigatórios.")
        return [], base_session_dir

    if len(urls) > 10:
        st.error("Por favor, insira no máximo 10 URLs.")
        return [], base_session_dir

    # Gera um ID único para o controle
    id_unico = IDGenerator.generate_control_id(vendor, tecnologia, datetime.now().year, 1)
    st.info(f"ID do controle gerado: {id_unico}")

    # Gera run_id para criar um subdiretório
    run_id = IDGenerator.generate_uuid()
    run_short_id = run_id[:8]

    # Novo subdiretório
    run_artifacts_dir = base_session_dir / f"r_{run_short_id}"
    run_artifacts_dir.mkdir(parents=True, exist_ok=True)

    # (Opcional) Inicializa/Reaproveita assistente
    assistant_id = OpenAIService.initialize_assistant("config/config.json", selected_language)

    # Novo URLProcessor para este run (não usará run_id no nome do arquivo, mas salva na pasta r_<id>)
    run_url_processor = URLProcessor(str(run_artifacts_dir), run_short_id)

    # 1) Baixa e salva as URLs como Markdown
    markdown_files = []
    for url in urls:
        html_content = run_url_processor.fetch_page_content(url)
        if html_content:
            markdown_path = run_url_processor.save_as_markdown(url, html_content)
            markdown_files.append(Path(markdown_path))
            st.success(f"URL processada com sucesso: {url}")
        else:
            st.warning(f"Falha ao processar URL: {url}")

    if not markdown_files:
        st.error("Nenhum arquivo Markdown foi gerado. Verifique as URLs fornecidas.")
        return [], run_artifacts_dir

    # 2) Executa o AgentProcessor
    agent_processor = AgentProcessor(
        config_loader,
        selected_language,
        run_artifacts_dir
    )
    final_content = agent_processor.process_files(markdown_files)

    # 3) Salva o resultado final
    final_markdown_path = run_artifacts_dir / f"r_{run_short_id}_final.md"
    final_markdown_path.write_text(final_content, encoding="utf-8")

    # 4) Gera HTML
    html_content = generate_baseline_html(
        html_generator,
        config_loader,
        selected_language,
        str(final_markdown_path),
        run_artifacts_dir,
        run_short_id
    )

    # Disponibiliza para download
    st.success("Baseline gerado com sucesso!")
    st.download_button(
        label="Download Web Page",
        data=html_content,
        file_name=f"r_{run_short_id}_controls.html",
        mime="text/html",
    )

    # Retorna infos para logs externos ou limpeza
    generated_files = [
        str(final_markdown_path),
        str(run_artifacts_dir / f"r_{run_short_id}_final.html")
    ]
    return generated_files, run_artifacts_dir


def main():
    st.title("BaselineForge")

    selected_language = st.selectbox(
        "Selecione o idioma desejado | Select the desired language | Seleccione el idioma deseado:",
        ["EN-US", "PT-BR", "ES-ES"]
    )

    # Inicializa as dependências e obtem short_session_id
    config_loader, url_processor, html_generator, menu_config, base_session_dir, short_session_id = initialize_dependencies(selected_language)

    # Roda todo o pipeline
    generated_files, artifacts_dir = run_pipeline(
        config_loader,
        url_processor,
        html_generator,
        menu_config,
        base_session_dir,
        selected_language,
        short_session_id
    )

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
