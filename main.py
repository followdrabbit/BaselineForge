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


def process_urls(urls: List[str], url_processor: URLProcessor) -> List[Path]:
    """
    Processa as URLs, buscando o conteúdo HTML e salvando em arquivos Markdown.
    Retorna uma lista de caminhos (Path) dos arquivos gerados.
    """
    markdown_files = []
    for url in urls:
        html_content = url_processor.fetch_page_content(url)
        if html_content:
            markdown_path = url_processor.save_as_markdown(url, html_content)
            markdown_files.append(Path(markdown_path))
            st.success(f"URL processada com sucesso: {url}")
        else:
            st.warning(f"Falha ao processar URL: {url}")
    return markdown_files


def generate_baseline_html(
    html_generator: HTMLGenerator,
    config_loader: ConfigLoader,
    selected_language: str,
    final_markdown_path: str,
    artifacts_dir: Path,
    session_id: str
) -> str:
    """
    Gera o HTML final do baseline utilizando um template e dados de configuração.
    Retorna o conteúdo HTML gerado.
    """
    template_path = "templates/template_html.html"
    output_html_path = artifacts_dir / f"{session_id}_final.html"
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


def initialize_dependencies(selected_language: str) -> Tuple[ConfigLoader, URLProcessor, HTMLGenerator, dict, Path, str]:
    """
    Inicializa as dependências da aplicação garantindo que apenas UM session_id seja gerado por execução.
    """
    config_loader = ConfigLoader(config_file="config/config.json")

    try:
        menu_config = config_loader.get_menu(selected_language)
    except Exception as e:
        st.error(f"Erro ao carregar as configurações do idioma {selected_language}: {e}")
        st.stop()

    # Garante que apenas um session_id seja criado por execução do script
    if "session_id" not in st.session_state:
        st.session_state.session_id = IDGenerator.generate_uuid()

    session_id = st.session_state.session_id  # Reutilizando session_id existente
    artifacts_dir = Path("artefacts") / f"session_{session_id}"
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Passamos o mesmo session_id para todas as instâncias
    url_processor = URLProcessor(str(artifacts_dir), session_id)
    html_generator = HTMLGenerator()

    return config_loader, url_processor, html_generator, menu_config, artifacts_dir, session_id


def get_user_inputs(menu_config: dict) -> Tuple[str, str, List[str]]:
    """
    Coleta os inputs do usuário (fornecedor, tecnologia e URLs) usando o menu de configuração.
    """
    vendor = st.selectbox(menu_config.get("select_vendor", "Selecione o Fornecedor"),
                          ["AWS", "Azure", "GCP", "Huawei", "OCI"])
    tecnologia = st.text_input(menu_config.get("enter_technology_name", "Digite o nome da Tecnologia"))
    urls_input = st.text_area(menu_config.get("enter_urls", "Digite até 10 URLs separadas por vírgula"), "")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    return vendor, tecnologia, urls


def run_pipeline(config_loader: ConfigLoader, url_processor: URLProcessor, html_generator: HTMLGenerator,
                 menu_config: dict, artifacts_dir: Path, selected_language: str, session_id: str) -> Tuple[List[str], Path]:
    """
    Executa todo o pipeline para gerar o baseline garantindo que o session_id seja único na execução.
    """
    vendor, tecnologia, urls = get_user_inputs(menu_config)

    with st.form("Formulário de ID"):
        submit_button = st.form_submit_button(menu_config.get("generate_baseline", "Gerar Baseline"))

    if not submit_button:
        st.info("Aguardando submissão do formulário...")
        return [], artifacts_dir

    if not (vendor and tecnologia and urls):
        st.error("Por favor, preencha todos os campos obrigatórios.")
        return [], artifacts_dir

    if len(urls) > 10:
        st.error("Por favor, insira no máximo 10 URLs.")
        return [], artifacts_dir

    # Gera um ID único para o controle
    id_unico = IDGenerator.generate_control_id(vendor, tecnologia, datetime.now().year, 1)
    st.info(f"ID do controle gerado: {id_unico}")

    # Inicializa o assistente baseado no idioma selecionado
    assistant_id = OpenAIService.initialize_assistant("config/config.json", selected_language)

    # Processa as URLs e gera arquivos Markdown
    markdown_files = process_urls(urls, url_processor)
    if not markdown_files:
        st.error("Nenhum arquivo Markdown foi gerado. Verifique as URLs fornecidas.")
        return [], artifacts_dir

    # Processa os arquivos usando o AgentProcessor
    agent_processor = AgentProcessor(config_loader, selected_language, artifacts_dir)
    final_content = agent_processor.process_files(markdown_files, id_unico)

    # Salva o conteúdo final consolidado
    final_output_path = artifacts_dir / f"{id_unico}_final.md"
    with final_output_path.open("w", encoding="utf-8") as f:
        f.write(final_content)

    # Gera o HTML final do baseline
    html_content = generate_baseline_html(
        html_generator, config_loader, selected_language,
        str(final_output_path), artifacts_dir, session_id
    )

    st.success("Baseline gerado com sucesso")
    st.download_button(
        label="Download Web Page",
        data=html_content,
        file_name=f"{session_id}_controls.html",
        mime="text/html",
    )

    generated_files = [str(final_output_path), str(artifacts_dir / f"{session_id}_final.html")]
    return generated_files, artifacts_dir


def main():
    st.title("BaselineForge")

    selected_language = st.selectbox(
        "Selecione o idioma desejado | Select the desired language | Seleccione el idioma deseado:",
        ["EN-US", "PT-BR", "ES-ES"]
    )

    # Inicializa as dependências da aplicação garantindo um único session_id
    config_loader, url_processor, html_generator, menu_config, artifacts_dir, session_id = initialize_dependencies(selected_language)

    # Executa o pipeline de geração do baseline
    generated_files, artifacts_dir = run_pipeline(
        config_loader, url_processor, html_generator, menu_config, artifacts_dir, selected_language, session_id
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
