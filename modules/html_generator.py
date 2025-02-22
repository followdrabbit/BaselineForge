import os
from pathlib import Path
import markdown
from jinja2 import Template
from bs4 import BeautifulSoup
from datetime import datetime


class HTMLGenerator:
    """Class to handle HTML generation from Markdown content using templates."""

    @staticmethod
    def load_file(file_path: str) -> str:
        """Load the content of a file, ensuring it exists."""
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        return file.read_text(encoding="utf-8").strip()

    @staticmethod
    def markdown_to_html(md_content: str) -> str:
        """Convert Markdown content to HTML."""
        return markdown.markdown(md_content)

    @staticmethod
    def extract_controls_from_html(html_content: str) -> list:
        """Extract security controls from an HTML list structure."""
        soup = BeautifulSoup(html_content, "html.parser")
        controls = []
        
        for ul in soup.find_all("ul"):
            control = {
                li.find("strong").get_text(strip=True).replace(":", "").strip(): 
                li.get_text(strip=True).replace(f"{li.find('strong').get_text(strip=True)}:", "").strip()
                for li in ul.find_all("li") if li.find("strong")
            }
            if control:
                controls.append(control)
                
        return controls

    @staticmethod
    def controls_to_html_table(controls: list, headers: list) -> str:
        """Convert a list of controls to an HTML table."""
        if not controls:
            return "<p>No controls found in the Markdown content.</p>"

        table_rows = [
            "<tr>" + "".join(f"<td>{control.get(header, 'N/A')}</td>" for header in headers) + "</tr>"
            for control in controls
        ]

        return f"""
        <table id='controls_table'>
            <tr>{"".join(f"<th>{header}</th>" for header in headers)}</tr>
            {"".join(table_rows)}
        </table>
        """

    @staticmethod
    def generate_version_table(version_info: dict) -> str:
        """Generate the HTML for the version table."""
        required_keys = ["version", "status", "draft"]
        if not all(key in version_info for key in required_keys):
            raise ValueError("Missing required keys in version_info.")

        return f"""
        <table id="version_table">
            <tbody>
                <tr><th>Version</th><td>{version_info['version']}</td></tr>
                <tr><th>Status</th><td>{version_info['status']}</td></tr>
                <tr><th>Draft</th><td>{version_info['draft']}</td></tr>
            </tbody>
        </table>
        """

    @staticmethod
    def generate_history_table(datetime_str: str, controls_info: list, history_labels: dict) -> str:
        """Generate the HTML for the history table."""
        included_controls_html = "\n".join(
            f"<li>{control_id} - {control_title}</li>"
            for control_id, control_title in controls_info
        )

        return f"""
        <table id='history_table'>
            <thead>
                <tr>
                    <th>{history_labels.get('version', 'Version')}</th>
                    <th>{history_labels.get('revised_on', 'Revised On')}</th>
                    <th>{history_labels.get('description', 'Description')}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>1.0</strong></td>
                    <td><strong>{datetime_str}</strong></td>
                    <td>
                        <p><strong>{history_labels.get('short_description', 'Short Description')}</strong>: {history_labels.get('short_description_content', 'Document Created')}</p>
                        <p><strong>{history_labels.get('excluded_controls', 'Excluded Controls')}</strong>: {history_labels.get('excluded_controls_content', 'None')}</p>
                        <p><strong>{history_labels.get('included_controls', 'Included Controls')}</strong>:</p>
                        <ul>{included_controls_html}</ul>
                    </td>
                </tr>
            </tbody>
        </table>
        """

    @staticmethod
    def generate_html(
        template_path: str,
        content_path: str,
        output_html: str,
        html_sections: dict,
        history_table: dict,
        control_table_labels: dict,
        version_info: dict
    ) -> str:
        """Generate an HTML file from a Markdown file using a template."""
        try:
            template_content = HTMLGenerator.load_file(template_path)
            markdown_content = HTMLGenerator.load_file(content_path)
        except FileNotFoundError as e:
            return str(e)

        html_content = HTMLGenerator.markdown_to_html(markdown_content)
        controls = HTMLGenerator.extract_controls_from_html(html_content)

        # Headers from control table labels
        headers = [control_table_labels.get(k, k) for k in ["ID", "TITLE", "DESCRIPTION", "APPLICABILITY", "SECURITY_RISK", "CRITICALITY", "REFERENCES"]]
        controls_table = HTMLGenerator.controls_to_html_table(controls, headers)

        controls_info = [(c.get(headers[0], "N/A"), c.get(headers[1], "N/A")) for c in controls]
        datetime_str = datetime.now().strftime("%Y-%m-%d")
        history_table_html = HTMLGenerator.generate_history_table(datetime_str, controls_info, history_table)
        version_table_html = HTMLGenerator.generate_version_table(version_info)

        template = Template(template_content)
        final_html = template.render(
            title="Security Baseline Report",
            control_list_title=html_sections.get("control_list_title", "Security Controls List"),
            controls_table_content=controls_table,
            history_table_title=html_sections.get("history_table_title", "Change History"),
            history_table_content=history_table_html,
            version_table_content=version_table_html
        )

        # Save output HTML
        try:
            with open(output_html, "w", encoding="utf-8") as file:
                file.write(final_html)
        except Exception as e:
            return f"Error writing file: {str(e)}"

        return final_html
