import streamlit as st
from datetime import datetime
import os
from modules.config_loader import ConfigLoader
from modules.url_processor import URLProcessor
from modules.id_generator import IDGenerator  # Corrigido: Garantir a importação correta
from modules.openai_service import OpenAIService
from modules.html_generator import HTMLGenerator
from modules.cleanup_util import cleanup_generated_files
from modules.prompt_processor import PromptProcessor

# Variáveis globais para rastrear arquivos e o diretório da sessão
generated_files = []  # Para rastrear os arquivos criados durante a execução
ARTIFACTS_DIRECTORY = ""  # Diretório da sessão atual


def main():
    global generated_files, ARTIFACTS_DIRECTORY
    st.title("BaselineForge")

    # Geração de UUID único para a sessão
    section_id = IDGenerator.generate_uuid()  # Corrigido: Inicialização correta do IDGenerator

    # Diretório para artefatos
    ARTIFACTS_DIRECTORY = os.path.join("artefacts", f"session_{section_id}")
    os.makedirs(ARTIFACTS_DIRECTORY, exist_ok=True)

    # Inicializar carregadores e utilitários
    config_loader = ConfigLoader(config_file="config/config.json")
    url_processor = URLProcessor(ARTIFACTS_DIRECTORY)
    html_generator = HTMLGenerator()

    # Seleção de idioma
    selected_language = st.selectbox(
        "Select the desired language | Selecione o idioma desejado | Seleccione el idioma deseado:",
        ["EN-US", "PT-BR", "ES-ES"]
    )

    # Carregar configurações do idioma selecionado
    try:
        menu_config = config_loader.get_menu(selected_language)
        categories = config_loader.get_categories(selected_language)

        if not categories or not isinstance(categories, list):
            st.warning("Nenhuma categoria válida encontrada no arquivo de configuração.")
            categories = ["Default Category"]

    except KeyError as e:
        st.error(f"Erro na estrutura do arquivo de configuração para o idioma {selected_language}: {e}")
        st.stop()
    except Exception as e:
        st.error(f"Erro ao carregar configurações do idioma {selected_language}: {e}")
        st.stop()

    # Configuração inicial do formulário
    vendor = st.selectbox(menu_config.get("select_vendor", "Select Vendor"), ["AWS", "Azure", "GCP", "Huawei", "OCI"])
    tecnologia = st.text_input(menu_config.get("enter_technology_name", "Enter the Technology Name"))
    versao = st.text_input(
        menu_config.get("enter_technology_version", "Enter the version of the technology (or leave 'Static' if the technology has no version)"),
        "Static"
    )
    categoria = st.selectbox(menu_config.get("select_category", "Select Category"), [""] + categories)
    urls_input = st.text_area(menu_config.get("enter_urls", "Enter up to 10 URLs separated by commas"), "")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    ano_atual = datetime.now().year

    # Formulário para gerar ID
    with st.form("Formulário de ID"):
        submit_button = st.form_submit_button(menu_config.get("generate_baseline", "Generate Baseline"))

    if submit_button:
        if vendor and tecnologia and categoria != "" and versao and urls:
            if len(urls) > 10:
                st.error("Por favor, insira no máximo 10 URLs.")
                return

            # Geração do ID
            id_unico = IDGenerator.generate_id(vendor, categoria, tecnologia, versao, ano_atual, 1)

            markdown_files = []
            creation_responses_unified = ""

            # Inicializar OpenAI Assistant
            assistant_id = OpenAIService.initialize_assistant("config/config.json")
            processor = PromptProcessor(assistant_id)

            try:
                # Processar URLs e gerar arquivos Markdown
                st.info("Inciando o processamento da(s) URL(s)...")
                for url in urls:
                    html_content = url_processor.fetch_page_content(url)
                    if html_content:
                        markdown_path = url_processor.save_as_markdown(url, html_content, section_id)
                        markdown_files.append(markdown_path)
                        generated_files.append(markdown_path)
                        st.success(f"URL: {url} processada com sucesso")
                    else:
                        st.warning(f"Falha ao processar URL: {url}")

                if not markdown_files:
                    st.error("Nenhum arquivo Markdown foi gerado. Verifique as URLs fornecidas.")
                    return

                # Processar cada arquivo Markdown individualmente com o primeiro prompt
                st.info("Inciando a extração dos controles...")
                for markdown_file in markdown_files:
                    with open(markdown_file, "r", encoding="utf-8") as file:
                        markdown_content = file.read()

                    # Processar o prompt de criação dos controles
                    creation_output_path, creation_responses = processor.process_prompt(
                        prompt=f"ID: {id_unico}\n{config_loader.get_prompts(selected_language)[0]}",
                        content=markdown_content,
                        output_file=os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_responses.md")
                    )
                    creation_responses_unified += "\n".join(creation_responses) + "\n"

                st.success("Controles extraídos com sucesso")

                # Processar o prompt de consolidação dos controles
                st.info("Inciando a consolidação dos controles...")
                consolidation_output_path, consolidation_output_responses = processor.process_prompt(
                    prompt=config_loader.get_prompts(selected_language)[1],
                    content=creation_responses_unified,
                    output_file=os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_consolidate.md")
                )
                st.success("Controles consolidados com sucesso.")

                # Processar o prompt de revisão dos controles
                st.info("Inciando a revisão dos controles...")
                review_output_path, review_output_responses = processor.process_prompt(
                    prompt=config_loader.get_prompts(selected_language)[2],
                    content=consolidation_output_responses,
                    output_file=os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_final.md")
                )
                st.success("Controles revisados com sucesso.")

                generated_files.extend([creation_output_path, consolidation_output_path, review_output_path])

                # Gerar HTML final
                st.info("Gerando Baseline...")
                template_path = "templates/template_html.html"
                output_html_path = os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_final.html")
                html_sections = config_loader.get_html_sections(selected_language)
                version_info = config_loader.get_version_info(selected_language)
                history_table = config_loader.get_history_table(selected_language)
                control_table_labels = config_loader.get_control_table(selected_language)

                html_content = html_generator.generate_html(
                    template_path=template_path,
                    content_path=review_output_path,
                    output_html=output_html_path,
                    html_sections=html_sections,
                    history_table=history_table,
                    control_table_labels=control_table_labels,
                    version_info=version_info
                )
                generated_files.append(output_html_path)

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

if __name__ == "__main__":
    try:
        main()
    finally:
        # Limpar arquivos e diretório da sessão após a execução
        cleanup_generated_files(generated_files, ARTIFACTS_DIRECTORY)