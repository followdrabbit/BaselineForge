from pathlib import Path
import streamlit as st
from modules.openai_service import OpenAIService

class AgentProcessor:
    def __init__(self, config_loader, selected_language: str, vendor: str, artifacts_dir: Path):
        self.config_loader = config_loader
        self.selected_language = selected_language
        self.vendor = vendor
        self.artifacts_dir = artifacts_dir
        self.log_file_path = self.artifacts_dir / "agent.log"

        self.agents_config = self.config_loader.get("languages")[self.selected_language]["agents"].get(vendor, {})

    def _log_message(self, message: str):
        """Writes a log message to both the log file and the Streamlit app."""
        with self.log_file_path.open("a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
        st.write(message)

    def process_files(self, markdown_files: list) -> str:
        """Processes the files through a sequence of AI agents."""
        st.subheader("🚀 Starting baseline creation")

        self._log_message("📌 **[STEP 1/5] Extracting requirements**")
        for md_file in markdown_files:
            original_text = self._read_file_content(md_file)
            self.run_agent("Requisitor", original_text, md_file)

        self._log_message("📌 **[STEP 2/5] Transforming requirements into automatable controls**")
        controlgen_outputs = []
        for md_file in markdown_files:
            requisitor_file = self.artifacts_dir / f"{md_file.stem}_Requisitor.md"
            requisitor_output = self._read_file_content(requisitor_file)

            gen_out = self.run_agent("ControlGen", requisitor_output, md_file)
            controlgen_outputs.append(gen_out)

        self._log_message("📌 **[STEP 3/5] Unifying controls**")
        unified_controlgen = "\n\n".join(
            f"### ControlGen Output - File {idx+1}\n{text}"
            for idx, text in enumerate(controlgen_outputs)
        )
        controlgen_merged_file = self.artifacts_dir / "controlgen_unified.md"
        controlgen_merged_file.write_text(unified_controlgen, encoding="utf-8")

        self._log_message("📌 **[STEP 4/5] Refining Controls**")
        refiner_out = self.run_agent("ControlRefiner", unified_controlgen, controlgen_merged_file)

        self._log_message("📌 **[STEP 5/5] Evaluating Risks**")
        final_out = self.run_agent("RiskEvaluator", refiner_out, controlgen_merged_file)
        return final_out

    def run_agent(self, agent_name: str, content: str, md_file: Path) -> str:
        """Runs an AI agent and logs the token usage and cost."""
        agent_info = self.agents_config.get(agent_name)
        if not agent_info:
            self._log_message(f"⚠️ [WARNING] Agent `{agent_name}` not configured. Skipping.")
            return content

        agent_id = agent_info.get("identifier", "")
        if not agent_id or "PLACEHOLDER" in agent_id:
            self._log_message(f"⚠️ [WARNING] Agent `{agent_name}` has no valid identifier. Skipping.")
            return content
        
        prompt = f"Function: {agent_info['function']}\n\nContent:\n{content}"
        processed_content = "\n".join(OpenAIService.run_assistant(prompt, agent_id))
        output_path = self.artifacts_dir / f"{md_file.stem}_{agent_name}.md"
        output_path.write_text(processed_content, encoding="utf-8")

        return processed_content

    def _read_file_content(self, md_file: Path) -> str:
        if not md_file.exists():
            return ""
        return md_file.read_text(encoding="utf-8")
