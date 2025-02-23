import os
from pathlib import Path
from jinja2 import Template
from datetime import datetime
import pandas as pd

class HTMLGenerator:
    """Classe para gerar documentos HTML a partir de DataFrames e templates."""

    @staticmethod
    def load_file(file_path: str) -> str:
        """Carrega o conteúdo de um arquivo, garantindo que ele exista."""
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        return file.read_text(encoding="utf-8").strip()

    @staticmethod
    def dataframe_to_html_table(df: pd.DataFrame, table_id: str = "") -> str:
        """Converte um DataFrame pandas em uma tabela HTML."""
        if df.empty:
            return f"<p>No data available for {table_id}.</p>"
        headers = df.columns.tolist()
        header_html = "".join(f"<th>{header}</th>" for header in headers)
        rows_html = ""
        for _, row in df.iterrows():
            row_html = "".join(f"<td>{row[col]}</td>" for col in headers)
            rows_html += f"<tr>{row_html}</tr>"
        table_html = f"""
        <table id='{table_id}'>
            <thead>
                <tr>{header_html}</tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        """
        return table_html

    @staticmethod
    def generate_version_table(version_info: dict) -> str:
        """
        Gera a tabela de versão com as informações:
        Version e Status.
        """
        version = version_info.get("version", "N/A")
        status = version_info.get("status", "N/A")
        return f"""
        <table id="version_table">
            <tbody>
                <tr><th>Version</th><td>{version}</td></tr>
                <tr><th>Status</th><td>{status}</td></tr>
            </tbody>
        </table>
        """

    @staticmethod
    def generate_security_controls_table(controls_df: pd.DataFrame, risks_df: pd.DataFrame, base_control_id: str) -> str:
        """
        Mescla os DataFrames de controles e riscos usando o campo "Title" como chave
        e gera uma tabela HTML com as colunas:
        ID | Title | Description | Applicability | Security Risk | Default Behavior / Limitations | Automation | References |
        Risk Description | Impact Analysis | Confidentiality | Integrity | Availability |
        Regulatory & Compliance Impact | Likelihood of Exploitation | Detection and Mitigation Difficulty | Risk Level

        Se os dados não possuírem a coluna "ID", ela será gerada a partir do base_control_id.
        """
        # Mescla os DataFrames com base na coluna "Title"
        merged_df = pd.merge(controls_df, risks_df, on="Title", how="outer", suffixes=("", "_risk"))
        # Se a coluna "ID" não existir, gera-a usando o padrão base_control_id
        if "ID" not in merged_df.columns:
            # Supondo que base_control_id siga o padrão "VENDOR-TECHNOLOGY-YEAR-0001"
            prefix = base_control_id[:-4]  # Remove os últimos 4 dígitos (o contador)
            count = len(merged_df)
            merged_df.insert(0, "ID", [f"{prefix}{i+1:04d}" for i in range(count)])
        
        # Define a ordem desejada das colunas
        desired_columns = [
            "ID", "Title", "Description", "Applicability", "Security Risk", 
            "Default Behavior / Limitations", "Automation", "References",
            "Risk Description", "Impact Analysis", "Regulatory & Compliance Impact",
            "Likelihood of Exploitation", "Detection and Mitigation Difficulty", "Risk Level"
        ]
        # Cria um novo DataFrame com essas colunas, preenchendo com "N/A" se necessário
        final_data = {}
        for col in desired_columns:
            if col in merged_df.columns:
                final_data[col] = merged_df[col]
            else:
                final_data[col] = ["N/A"] * len(merged_df)
        final_df = pd.DataFrame(final_data)
        return HTMLGenerator.dataframe_to_html_table(final_df, table_id="controls_table")

    @staticmethod
    def generate_change_history_table(controls_df: pd.DataFrame, history_config: dict, version_info: dict) -> str:
        """
        Gera a tabela de Change History com as colunas:
        VERSION | REVISED ON | DESCRIPTION

        A DESCRIPTION é construída com:
          - Short Description: (usando os campos 'short_description' e 'short_description_content')
          - Excluded Controls: (usando 'excluded_controls' e 'excluded_controls_content')
          - Included Controls: listando todos os Titles dos controles.
        """
        version = version_info.get("version", "N/A")
        revised_on = datetime.now().strftime("%Y-%m-%d")
        short_desc = history_config.get("short_description", "Short Description") + ": " + history_config.get("short_description_content", "Document Created")
        excluded = history_config.get("excluded_controls", "Excluded Controls") + ": " + history_config.get("excluded_controls_content", "None")
        included_controls = controls_df["Title"].tolist() if "Title" in controls_df.columns else []
        included = history_config.get("included_controls", "Included Controls") + ":<br>" + "<br>".join(f"- {title}" for title in included_controls)
        description = f"{short_desc}<br>{excluded}<br>{included}"
        df_history = pd.DataFrame({
            "VERSION": [version],
            "REVISED ON": [revised_on],
            "DESCRIPTION": [description]
        })
        return HTMLGenerator.dataframe_to_html_table(df_history, table_id="history_table")

    @staticmethod
    def generate_html(
        template_path: str,
        output_html: str,
        html_sections: dict,
        version_info: dict,
        controls_df: pd.DataFrame,
        risks_df: pd.DataFrame,
        history_config: dict,
        base_control_id: str
    ) -> str:
        """
        Gera o documento HTML final seguindo a estrutura:
          - Tabela de Versão (com Version e Status)
          - Título "SECURITY CONTROLS" e tabela de controles (mesclando controles e riscos e gerando a coluna ID conforme o padrão)
          - Título "Change History" e tabela de histórico de alterações
        """
        try:
            template_content = HTMLGenerator.load_file(template_path)
        except FileNotFoundError as e:
            return str(e)
        version_table_html = HTMLGenerator.generate_version_table(version_info)
        security_controls_html = HTMLGenerator.generate_security_controls_table(controls_df, risks_df, base_control_id)
        change_history_html = HTMLGenerator.generate_change_history_table(controls_df, history_config, version_info)
        template = Template(template_content)
        final_html = template.render(
            title="Security Baseline Report",
            version_table_content=version_table_html,
            control_list_title=html_sections.get("control_list_title", "SECURITY CONTROLS"),
            controls_table_content=security_controls_html,
            history_table_title=html_sections.get("history_table_title", "Change History"),
            history_table_content=change_history_html
        )
        try:
            with open(output_html, "w", encoding="utf-8") as file:
                file.write(final_html)
        except Exception as e:
            return f"Error writing file: {str(e)}"
        return final_html
