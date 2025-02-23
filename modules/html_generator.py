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
            row_html = ""
            for col in headers:
                # Se for a coluna DESCRIPTION da tabela de histórico, permite a renderização do HTML (alinhamento à esquerda)
                if table_id == "history_table" and col.upper() == "DESCRIPTION":
                    row_html += f"<td>{row[col]}</td>"
                else:
                    row_html += f"<td>{row[col]}</td>"
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
    def get_merged_controls(controls_df: pd.DataFrame, risks_df: pd.DataFrame, base_control_id: str) -> pd.DataFrame:
        """
        Mescla os DataFrames de controles e riscos usando a coluna "Title" como chave.
        Se a coluna "ID" não existir, ela é criada utilizando o base_control_id como prefixo.
        Antes de fazer o merge, as colunas "Title" de ambos os dataframes são normalizadas (remoção de espaços extras e conversão para minúsculas)
        para garantir a correspondência correta.
        """
        # Normaliza a coluna 'Title' em ambos os dataframes
        controls_df["Title"] = controls_df["Title"].astype(str).str.strip().str.lower()
        risks_df["Title"] = risks_df["Title"].astype(str).str.strip().str.lower()

        merged_df = pd.merge(controls_df, risks_df, on="Title", how="outer", suffixes=("", "_risk"))
        if "ID" not in merged_df.columns:
            # Considera que o base_control_id segue o padrão "VENDOR-TECHNOLOGY-YEAR-0001"
            prefix = base_control_id[:-4]  # Remove os últimos 4 dígitos (o contador)
            count = len(merged_df)
            merged_df.insert(0, "ID", [f"{prefix}{i+1:04d}" for i in range(count)])
        return merged_df

    @staticmethod
    def generate_security_controls_table(controls_df: pd.DataFrame, risks_df: pd.DataFrame, base_control_id: str) -> str:
        """
        Gera a tabela de SECURITY CONTROLS mesclando os DataFrames de controles e riscos.
        As colunas geradas incluem ID, Title, Description, entre outras.
        Se a coluna "ID" não existir, ela é criada utilizando o base_control_id.
        """
        merged_df = HTMLGenerator.get_merged_controls(controls_df, risks_df, base_control_id)
        desired_columns = [
            "ID", "Title", "Description", "Applicability", "Security Risk", 
            "Default Behavior / Limitations", "Automation", "References",
            "Risk Description", "Impact Analysis", "Regulatory & Compliance Impact",
            "Likelihood of Exploitation", "Detection and Mitigation Difficulty", "Risk Level"
        ]
        final_data = {}
        for col in desired_columns:
            if col in merged_df.columns:
                final_data[col] = merged_df[col]
            else:
                final_data[col] = ["N/A"] * len(merged_df)
        final_df = pd.DataFrame(final_data)
        return HTMLGenerator.dataframe_to_html_table(final_df, table_id="controls_table")

    @staticmethod
    def generate_change_history_table(controls_df: pd.DataFrame, risks_df: pd.DataFrame, history_config: dict, version_info: dict, base_control_id: str) -> str:
        """
        Gera a tabela de Change History com as colunas:
        VERSION | REVISED ON | DESCRIPTION

        A DESCRIPTION é construída utilizando:
          - Short Description: (usando 'short_description' e 'short_description_content')
          - Excluded Controls: (usando 'excluded_controls' e 'excluded_controls_content')
          - Included Controls: listando os controles no formato "- Control_ID: Control_Title",
            apresentados como uma lista (ul/li) e com o conteúdo alinhado à esquerda.
        """
        merged_df = HTMLGenerator.get_merged_controls(controls_df, risks_df, base_control_id)
        version = version_info.get("version", "N/A")
        revised_on = datetime.now().strftime("%Y-%m-%d")
        short_desc = history_config.get("short_description", "Short Description") + ": " + history_config.get("short_description_content", "Document Created")
        excluded = history_config.get("excluded_controls", "Excluded Controls") + ": " + history_config.get("excluded_controls_content", "None")
        
        if "ID" in merged_df.columns:
            list_items = "".join(f"<li>{row['ID']}: {row['Title']}</li>" for _, row in merged_df.iterrows())
        else:
            list_items = "".join(f"<li>{title}</li>" for title in merged_df["Title"].tolist())
        included = history_config.get("included_controls", "Included Controls") + ":<br>" + "<ul>" + list_items + "</ul>"
        
        # Envolve toda a descrição em uma div com estilo para alinhamento à esquerda
        description = f"<div style='text-align: left;'>{short_desc}<br>{excluded}<br>{included}</div>"
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
        Gera o documento HTML final com:
          - Tabela de Versão
          - Título "SECURITY CONTROLS" e a tabela de controles (usando a mesclagem com riscos e o ID consistente)
          - Título "Change History" e a tabela de histórico de alterações (utilizando os mesmos IDs)
        """
        try:
            template_content = HTMLGenerator.load_file(template_path)
        except FileNotFoundError as e:
            return str(e)
        version_table_html = HTMLGenerator.generate_version_table(version_info)
        security_controls_html = HTMLGenerator.generate_security_controls_table(controls_df, risks_df, base_control_id)
        change_history_html = HTMLGenerator.generate_change_history_table(controls_df, risks_df, history_config, version_info, base_control_id)
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
