import streamlit as st
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

from modules.config_loader import ConfigLoader
from modules.url_processor import URLProcessor
from modules.id_generator import IDGenerator  # Agora deve implementar generate_control_id
from modules.openai_service import OpenAIService
from modules.html_generator import HTMLGenerator
from modules.cleanup_util import cleanup_generated_files
from modules.prompt_processor import PromptProcessor


def process_urls(urls: List[str], section_id: str, url_processor: URLProcessor) -> List[Path]:
    """
    Processa as URLs, buscando o conteúdo HTML e salvando em arquivos Markdown.
    Retorna uma lista de caminhos (Path) dos arquivos gerados.
    """
    markdown_files = []
    for url in urls:
        html_content = url_processor.fetch_page_content(url)
        if html_content:
            markdown_path = url_processor.save_as_markdown(url, html_content, section_id)
            markdown_files.append(Path(markdown_path))
            st.success(f"URL: {url} processada com sucesso")
        else:
            st.warning(f"Falha ao processar URL: {url}")
    return markdown_files


def process_prompts(
    processor: PromptProcessor,
    config_loader: ConfigLoader,
    selected_language: str,
    markdown_files: List[Path],
    id_unico: str,
    artifacts_dir: Path
) -> Tuple[str, str, str]:
    """
    Processa os prompts de extração, consolidação e revisão.
    Retorna os caminhos dos arquivos gerados para cada etapa.
    """
    creation_responses_unified = ""
    # Extração dos controles
    for md_file in markdown_files:
        with md_file.open("r", encoding="utf-8") as file:
            markdown_content = file.read()
        prompt_creation = f"ID: {id_unico}\n{config_loader.get_prompts(selected_language)[0]}"
        creation_output_path, creation_responses = processor.process_prompt(
            prompt=prompt_creation,
            content=markdown_content,
            output_file=str(artifacts_dir / f"{md_file.stem}_responses.md")
        )
        creation_responses_unified += "\n".join(creation_responses) + "\n"

    # Consolidação dos controles
    consolidation_output_path, consolidation_output_responses = processor.process_prompt(
        prompt=config_loader.get_prompts(selected_language)[1],
        content=creation_responses_unified,
        output_file=str(artifacts_dir / f"{id_unico}_consolidate.md")
    )

    # Revisão dos controles
    review_output_path, review_output_responses = processor.process_prompt(
        prompt=config_loader.get_prompts(selected_language)[2],
        content=consolidation_output_responses,
        output_file=str(artifacts_dir / f"{id_unico}_final.md")
    )
    return creation_output_path, consolidation_output_path, review_output_path


def generate_baseline_html(
    html_generator: HTMLGenerator,
    config_loader: ConfigLoader,
    selected_language: str,
    review_output_path: str,
    artifacts_dir: Path,
    section_id: str
) -> str:
    """
    Gera o HTML final do baseline utilizando um template e dados de configuração.
    Retorna o conteúdo HTML gerado.
    """
    template_path = "templates/template_html.html"
    output_html_path = artifacts_dir / f"{section_id}_final.html"
    html_sections = config_loader.get_html_sections(selected_language)
    version_info = config_loader.get_version_info(selected_language)
    history_table = config_loader.get_history_table(selected_language)
    control_table_labels = config_loader.get_control_table(selected_language)
    html_content = html_generator.generate_html(
        template_path=template_path,
        content_path=review_output_path,
        output_html=str(output_html_path),
        html_sections=html_sections,
        history_table=history_table,
        control_table_labels=control_table_labels,
        version_info=version_info
    )
    return html_content


def main():
    st.title("BaselineForge")
    section_id = IDGenerator.generate_uuid()
    artifacts_dir = Path("artefacts") / f"session_{section_id}"
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    config_loader = ConfigLoader(config_file="config/config.json")
    url_processor = URLProcessor(str(artifacts_dir))
    html_generator = HTMLGenerator()

    selected_language = st.selectbox(
        "Select the desired language | Selecione o idioma desejado | Seleccione el idioma deseado:",
        ["EN-US", "PT-BR", "ES-ES"]
    )

    # Carregar configurações do idioma selecionado
    try:
        menu_config = config_loader.get_menu(selected_language)
    except KeyError as e:
        st.error(f"Erro na estrutura do arquivo de configuração para o idioma {selected_language}: {e}")
        st.stop()
    except Exception as e:
        st.error(f"Erro ao carregar configurações do idioma {selected_language}: {e}")
        st.stop()

    vendor = st.selectbox(menu_config.get("select_vendor", "Select Vendor"), ["AWS", "Azure", "GCP", "Huawei", "OCI"])
    tecnologia = st.text_input(menu_config.get("enter_technology_name", "Enter the Technology Name"))
    urls_input = st.text_area(menu_config.get("enter_urls", "Enter up to 10 URLs separated by commas"), "")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    ano_atual = datetime.now().year

    with st.form("Formulário de ID"):
        submit_button = st.form_submit_button(menu_config.get("generate_baseline", "Generate Baseline"))

    if submit_button:
        if vendor and tecnologia and urls:
            if len(urls) > 10:
                st.error("Por favor, insira no máximo 10 URLs.")
                return generated_files, artifacts_dir

            # Gerar o ID do controle com o novo formato: VENDOR-SERVICE-YEAR-COUNTER
            id_unico = IDGenerator.generate_control_id(vendor, tecnologia, ano_atual, 1)
            st.info(f"ID do controle gerado: {id_unico}")

            # Inicializar o OpenAI Assistant
            assistant_id = OpenAIService.initialize_assistant("config/config.json")
            processor = PromptProcessor(assistant_id)

            try:
                st.info("Iniciando o processamento da(s) URL(s)...")
                markdown_files = process_urls(urls, section_id, url_processor)
                if not markdown_files:
                    st.error("Nenhum arquivo Markdown foi gerado. Verifique as URLs fornecidas.")
                    return generated_files, artifacts_dir

                st.info("Iniciando a extração dos controles...")
                creation_path, consolidation_path, review_path = process_prompts(
                    processor, config_loader, selected_language, markdown_files, id_unico, artifacts_dir
                )
                generated_files.extend([creation_path, consolidation_path, review_path])

                st.info("Gerando Baseline...")
                html_content = generate_baseline_html(
                    html_generator, config_loader, selected_language, review_path, artifacts_dir, section_id
                )
                generated_files.append(str(artifacts_dir / f"{section_id}_final.html"))

                if html_content:
                    st.success("Baseline gerado com sucesso")
                    st.download_button(
                        label="Download Web Page",
                        data=html_content,
                        file_name=f"{section_id}_controls.html",
                        mime="text/html",
                    )
            except Exception as e:
                st.error(f"Erro durante o processamento: {e}")
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")

    return generated_files, artifacts_dir


if __name__ == "__main__":
    # Define valores padrão para evitar NameError caso main() não retorne os valores esperados
    generated_files = []
    artifacts_dir = ""
    try:
        result = main()
        if result is not None:
            generated_files, artifacts_dir = result
    finally:
        cleanup_generated_files(generated_files, str(artifacts_dir))
