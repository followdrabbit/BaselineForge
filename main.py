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

def initialize_dependencies() -> Tuple[ConfigLoader, URLProcessor, HTMLGenerator, Path, str]:
    """
    Initializes the application's dependencies, ensuring that only ONE session_id is generated per session.
    The session_id is shortened to avoid path length issues on Windows.
    """
    config_loader = ConfigLoader(config_file="config/config.json")

    # Generate or get the session_id
    if "session_id" not in st.session_state:
        st.session_state.session_id = IDGenerator.generate_uuid()

    session_id = st.session_state.session_id
    short_session_id = session_id[:8]

    base_session_dir = Path("artefacts") / f"s_{short_session_id}"
    base_session_dir.mkdir(parents=True, exist_ok=True)

    url_processor = URLProcessor(str(base_session_dir), short_session_id)
    html_generator = HTMLGenerator()

    return config_loader, url_processor, html_generator, base_session_dir, short_session_id


def get_user_inputs() -> Tuple[str, str, List[str]]:
    """
    Collect user inputs (vendor, technology, and URLs) directly in the main.py, in English.
    """
    st.write("Please fill in the fields below to generate your baseline:")

    vendor_label = "Select your Cloud Provider (Vendor)"
    technology_label = "Enter your Technology Name"
    urls_label = "Enter up to 10 URLs, separated by commas"

    vendor = st.selectbox(vendor_label, ["AWS", "Azure", "GCP", "Huawei", "OCI"])
    technology = st.text_input(technology_label)
    urls_input = st.text_area(urls_label, "")
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]

    return vendor, technology, urls


def run_pipeline(
    config_loader: ConfigLoader,
    url_processor: URLProcessor,
    html_generator: HTMLGenerator,
    base_session_dir: Path
) -> Tuple[List[str], Path, str]:
    """
    Executes the entire pipeline to generate the baseline.
    On each click of the "Generate Baseline" button, it creates a subdirectory using run_id.
    Returns the list of generated files, the artifacts directory, and the unique ID (id_unico).
    """
    vendor, technology, urls = get_user_inputs()

    st.write("Click the button to generate the baseline:")
    with st.form("BaselineForm"):
        generate_button_label = "Generate Baseline"
        submit_button = st.form_submit_button(generate_button_label)

    if not submit_button:
        st.info("Waiting for form submission...")
        return [], base_session_dir, ""

    # Clear agent_costs BEFORE starting a new pipeline
    st.session_state["agent_costs"] = {}

    if not (vendor and technology and urls):
        st.error("Please fill in all required fields.")
        return [], base_session_dir, ""

    if len(urls) > 10:
        st.error("Please enter a maximum of 10 URLs.")
        return [], base_session_dir, ""

    # Generate a base ID for the controls
    id_unico = IDGenerator.generate_control_id(vendor, technology, datetime.now().year, 1)

    run_id = IDGenerator.generate_uuid()
    run_short_id = run_id[:8]

    run_artifacts_dir = base_session_dir / f"r_{run_short_id}_{id_unico}"
    run_artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Initialize the assistant (e.g., the "Requisitor" agent)
    assistant_id = OpenAIService.initialize_assistant("config/config.json", vendor, agent_name="Requisitor")

    # Prepare a URLProcessor specific to this "run"
    run_url_processor = URLProcessor(str(run_artifacts_dir), run_short_id)

    # Download and convert each URL to Markdown
    markdown_files = []
    for url in urls:
        html_content = run_url_processor.fetch_page_content(url)
        if html_content:
            markdown_path = run_url_processor.save_as_markdown(url, html_content)
            markdown_files.append(Path(markdown_path))
        else:
            st.warning(f"Failed to process URL: {url}")

    if not markdown_files:
        st.error("No Markdown file was generated. Please check the provided URLs.")
        return [], run_artifacts_dir, id_unico

    # Process files with the AgentProcessor
    agent_processor = AgentProcessor(config_loader, vendor, run_artifacts_dir)
    final_content, agent_costs = agent_processor.process_files(markdown_files)

    # Save the final output
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
            f"**Total Cost (agents' sum)**: US$ {total_cost:.4f}"
        )
    else:
        st.warning("No agent costs were recorded in st.session_state['agent_costs'].")

    return [str(final_markdown_path)], run_artifacts_dir, id_unico


def main():
    st.title("Welcome to BaselineForge")
    st.markdown("**Check out the project's GitHub repository:** [BaselineForge](https://github.com/followdrabbit/BaselineForge)")

    config_loader, url_processor, html_generator, base_session_dir, short_session_id = initialize_dependencies()

    generated_files, artifacts_dir, id_unico = run_pipeline(
        config_loader,
        url_processor,
        html_generator,
        base_session_dir
    )

    # (Optional) Generate final HTML if you want a downloadable report
    control_refiner_path = artifacts_dir / "controlgen_unified_ControlRefiner.md"
    risk_evaluator_path = artifacts_dir / "controlgen_unified_RiskEvaluator.md"
    if control_refiner_path.exists() and risk_evaluator_path.exists():
        df_controls = load_markdown_as_dataframe(str(control_refiner_path))
        df_risks = load_markdown_as_dataframe(str(risk_evaluator_path))

        # Hardcoded data for HTML sections (since we're not reading from config.json for these)
        html_sections = {
            "control_list_title": "Security Controls",
            "history_table_title": "Change History"
        }
        version_info = {
            "version": "1.0",
            "status": "Draft"
        }
        history_config = {
            "short_description": "Short Description",
            "short_description_content": "Document Created",
            "excluded_controls": "Excluded Controls",
            "excluded_controls_content": "None",
            "included_controls": "Included Controls"
        }

        html_content = html_generator.generate_html(
            template_path="templates/template_html.html",
            output_html=str(artifacts_dir / f"{id_unico}_final.html"),
            html_sections=html_sections,
            version_info=version_info,
            controls_df=df_controls,
            risks_df=df_risks,
            history_config=history_config,
            base_control_id=id_unico
        )

        st.download_button(
            label="Download Web Page",
            data=html_content,
            file_name=f"{id_unico}_controls.html",
            mime="text/html"
        )
    else:
        st.warning("Control and risk files were not found.")

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