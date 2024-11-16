import streamlit as st
from datetime import datetime
import os
from modules.config_loader import ConfigLoader
from modules.url_processor import URLProcessor
from modules.id_generator import IDGenerator
from modules.openai_service import OpenAIService
from modules.html_generator import HTMLGenerator
from modules.cleanup_util import cleanup_generated_files

# Variáveis globais para rastrear arquivos e o diretório da sessão
generated_files = []  # Para rastrear os arquivos criados durante a execução
ARTIFACTS_DIRECTORY = ""  # Diretório da sessão atual

def main():
    global generated_files, ARTIFACTS_DIRECTORY
    st.title("BaselineForge")

    # Geração de UUID único para a execução
    section_id = IDGenerator.generate_uuid()

    # Inicializa carregadores e utilitários
    openai_service = OpenAIService()
    html_generator = HTMLGenerator()

    # Inicializa o carregador de configuração
    config_loader = ConfigLoader(config_file="config/config.json")

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

    # Exibir título dinâmico de controle
    html_sections = config_loader.get_html_sections(selected_language)
    subheader_title = html_sections.get("control_list_title", "Security Controls List")
    st.subheader(subheader_title)

    # Diretório para artefatos
    ARTIFACTS_DIRECTORY = os.path.join("artefacts", f"session_{section_id}")
    os.makedirs(ARTIFACTS_DIRECTORY, exist_ok=True)


    # Inicializa o URLProcessor com o diretório da sessão
    url_processor = URLProcessor(ARTIFACTS_DIRECTORY)

    # Configuração inicial
    vendor = st.selectbox(menu_config.get("select_vendor", "Select Vendor"), ["AWS", "Azure", "GCP", "Huawei", "OCI"])
    tecnologia = st.text_input(menu_config.get("enter_technology_name", "Enter the Technology Name"))
    versao = st.text_input(menu_config.get(
        "enter_technology_version", 
        "Enter the version of the technology (or leave 'Static' if the technology has no version)"
    ), "Static")
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
            st.success(f"ID gerado: {id_unico}")

            # Processar URLs
            markdown_files = []
            for url in urls:
                html_content = url_processor.fetch_page_content(url)
                if html_content:
                    markdown_path = url_processor.save_as_markdown(url, html_content, section_id)
                    generated_files.append(markdown_path)  # Rastrear arquivo Markdown gerado
                    markdown_files.append(markdown_path)
                    st.write(f"Conteúdo Markdown salvo em: {markdown_path}")
                else:
                    st.warning(f"Falha ao processar URL: {url}")

            if not markdown_files:
                st.error("Nenhum arquivo Markdown foi gerado. Verifique as URLs fornecidas.")
                return

            # Inicializa o OpenAI Assistant
            try:
                assistant_id = openai_service.initialize_assistant("config/config.json")
                st.success(f"Assistant initialized successfully")
            except Exception as e:
                st.error(f"Error initializing assistant: {e}")
                return

            # Processar prompts
            try:
                prompt_criacao, prompt_consolidacao = config_loader.get_prompts(selected_language)

                if "Error" in prompt_criacao or "Error" in prompt_consolidacao:
                    st.error("One or more prompt files could not be loaded. Check the file paths.")
                else:
                    output_file = os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_responses.md")
                    for markdown_file in markdown_files:
                        with open(markdown_file, "r", encoding="utf-8") as file:
                            markdown_content = file.read()

                        combined_content = f"ID: {id_unico}\n{prompt_criacao}\n\n{markdown_content}"
                        responses = openai_service.run_assistant(combined_content, assistant_id)

                        with open(output_file, "a", encoding="utf-8") as response_file:
                            response_file.write("\n".join(responses) + "\n")
                            st.success("Prompt processing completed successfully!")

                if os.path.exists(output_file):
                    with open(output_file, "r", encoding="utf-8") as file:
                        consolidated_content = file.read()

                    combined_consolidation = f"ID: {id_unico}\n{prompt_consolidacao}\n\n{consolidated_content}"
                    final_responses = openai_service.run_assistant(combined_consolidation, assistant_id)

                    final_output_file = os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_final.md")
                    with open(final_output_file, "w", encoding="utf-8") as final_file:
                        final_file.write("\n".join(final_responses))

                    st.success("Processamento do prompt de consolidação concluído com sucesso!")
                else:
                    st.error("Nenhum conteúdo gerado para consolidação. Verifique o processamento anterior.")
            except ValueError as e:
                st.error(f"Erro ao carregar prompts: {e}")
            except Exception as e:
                st.error(f"Erro durante o processamento dos prompts: {e}")

            # Gerar HTML final
            template_path = "templates/template_html.html"
            final_output_file = os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_final.md")
            output_html = os.path.join(ARTIFACTS_DIRECTORY, f"{section_id}_final.html")
            generated_files.append(output_html)  # Rastrear arquivo HTML gerado

            if os.path.exists(final_output_file):
                history_table = config_loader.get_history_table(selected_language)
                control_table_labels = config_loader.get_control_table(selected_language)  # Rótulos dinâmicos
                html_content = html_generator.generate_html(
                    template_path=template_path,
                    content_path=final_output_file,
                    output_html=output_html,
                    html_sections=html_sections,
                    history_table=history_table,
                    control_table_labels=control_table_labels
                )

                if html_content:
                    st.download_button(
                        label="Baixar Página Web",
                        data=html_content,
                        file_name=f"{section_id}_controles.html",
                        mime="text/html",
                    )
                    st.success("Documento HTML gerado com sucesso!")
                else:
                    st.error("Erro ao gerar o documento HTML. Verifique o template ou o conteúdo do Markdown.")
            else:
                st.error("Arquivo final de Markdown para HTML não encontrado. Verifique se o processamento anterior foi concluído com sucesso.")


if __name__ == "__main__":
    try:
        main()
    finally:
        # Limpar arquivos e diretório da sessão após a execução
        cleanup_generated_files(generated_files, ARTIFACTS_DIRECTORY)
