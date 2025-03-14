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
    Initializes the application's dependencies, ensuring that only ONE session_id
    is generated per session. The session_id is shortened to avoid exceeding path
    limits on Windows.
    """
    config_loader = ConfigLoader(config_file="config/config.json")
    try:
        menu_config = config_loader.get_menu(selected_language)
    except Exception as e:
        st.error(f"Error loading settings for language '{selected_language}': {e}")
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


def get_user_inputs(menu_config: dict) -> Tuple[str, str, List[str]]:
    """
    Collects user inputs (vendor, technology, and URLs) using the configuration menu.
    """
    vendor = st.selectbox(
        menu_config.get("select_vendor", "Select the Vendor"),
        ["AWS", "Azure", "GCP", "Huawei", "OCI"]
    )
    technology = st.text_input(
        menu_config.get("enter_technology_name", "Enter the Technology Name")
    )
    urls_input = st.text_area(
        menu_config.get("enter_urls", "Enter up to 10 URLs separated by commas"), ""
    )
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    return vendor, technology, urls


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
    Generates the final baseline HTML using the HTMLGenerator.
    The run_short_id is used for naming the output file, and id_unico
    is passed to maintain the ID pattern in the SECURITY CONTROLS table.
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
        controls_df=load_markdown_as_dataframe(final_markdown_path.replace("final.md", "controlgen_unified_ControlRefiner.md")),
        risks_df=load_markdown_as_dataframe(final_markdown_path.replace("final.md", "controlgen_unified_RiskEvaluator.md")),
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
    Executes the entire pipeline to generate the baseline.
    Each click on "Generate Baseline" creates a subdirectory using run_id.
    Returns the list of generated files, the artifacts directory, and id_unico.
    """
    vendor, technology, urls = get_user_inputs(menu_config)
    with st.form("ID Form"):
        submit_button = st.form_submit_button(menu_config.get("generate_baseline", "Generate Baseline"))
    if not submit_button:
        st.info("Waiting for form submission...")
        return [], base_session_dir, ""
    
    # Clear agent_costs BEFORE starting a new pipeline
    st.session_state["agent_costs"] = {}

    if not (vendor and technology and urls):
        st.error("Please fill in all required fields.")
        return [], base_session_dir, ""
    if len(urls) > 10:
        st.error("Please enter at most 10 URLs.")
        return [], base_session_dir, ""

    # Generate a unique ID for the controls
    id_unico = IDGenerator.generate_control_id(vendor, technology, datetime.now().year, 1)

    run_id = IDGenerator.generate_uuid()
    run_short_id = run_id[:8]

    run_artifacts_dir = base_session_dir / f"r_{run_short_id}_{id_unico}"
    run_artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Initialize the Assistant
    assistant_id = OpenAIService.initialize_assistant("config/config.json", selected_language, vendor)
    run_url_processor = URLProcessor(str(run_artifacts_dir), run_short_id)

    markdown_files = []
    for url in urls:
        html_content = run_url_processor.fetch_page_content(url)
        if html_content:
            markdown_path = run_url_processor.save_as_markdown(url, html_content)
            markdown_files.append(Path(markdown_path))
        else:
            st.warning(f"Failed to process URL: {url}")

    if not markdown_files:
        st.error("No Markdown file was generated. Check the provided URLs.")
        return [], run_artifacts_dir, id_unico

    # Process the files through the agents
    agent_processor = AgentProcessor(config_loader, selected_language, vendor, run_artifacts_dir)
    final_content = agent_processor.process_files(markdown_files)

    # Save the final file
    final_markdown_path = run_artifacts_dir / f"r_{run_short_id}_final.md"
    final_markdown_path.write_text(final_content, encoding="utf-8")

    # Summarize and display the agent costs
    if "agent_costs" in st.session_state:
        total_cost = 0.0
        total_prompt_tokens = 0
        total_completion_tokens = 0

        for agent_name, agent_data in st.session_state["agent_costs"].items():
            total_cost += agent_data["total_cost"]
            total_prompt_tokens += agent_data["prompt_tokens"]
            total_completion_tokens += agent_data["completion_tokens"]

        st.info(
            f"**Prompt Tokens (sum)**: {total_prompt_tokens} | "
            f"**Completion Tokens (sum)**: {total_completion_tokens} | "
            f"**Approx. Total Cost (agents' sum)**: US$ {total_cost:.4f}"
        )
    else:
        st.warning("No agent costs were recorded in st.session_state['agent_costs'].")

    return [str(final_markdown_path)], run_artifacts_dir, id_unico


def main():
    st.title("BaselineForge")
    st.markdown(
        "**Check the project repository on GitHub:** "
        "[BaselineForge](https://github.com/followdrabbit/BaselineForge)"
    )

    selected_language = st.selectbox(
        "Select the desired language:",
        ["EN-US", "PT-BR", "ES-ES"]
    )

    (
        config_loader,
        url_processor,
        html_generator,
        menu_config,
        base_session_dir,
        short_session_id
    ) = initialize_dependencies(selected_language)

    generated_files, artifacts_dir, id_unico = run_pipeline(
        config_loader,
        url_processor,
        html_generator,
        menu_config,
        base_session_dir,
        selected_language,
        short_session_id
    )

    # If the control/refinement files exist, generate the HTML
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
        st.warning("No control or risk files were found.")

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
