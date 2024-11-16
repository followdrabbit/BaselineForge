import os
import markdown
from jinja2 import Template
from bs4 import BeautifulSoup
from datetime import datetime


class HTMLGenerator:
    """Class to handle HTML generation from Markdown content using templates."""

    @staticmethod
    def load_template(template_path: str) -> str:
        """Load the HTML template file."""
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template file not found: {template_path}")
        with open(template_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def load_file_content(file_path: str) -> str:
        """Load the content of a file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()

    @staticmethod
    def markdown_to_html(md_content: str) -> str:
        """Convert Markdown content to HTML."""
        return markdown.markdown(md_content)

    @staticmethod
    def extract_controls_from_html(html_content: str) -> list:
        """Extract control information from HTML content."""
        soup = BeautifulSoup(html_content, "html.parser")
        controls = []
        for ul in soup.find_all("ul"):
            control = {}
            for li in ul.find_all("li"):
                strong_tag = li.find("strong")
                if strong_tag:
                    key = strong_tag.get_text(strip=True).replace(":", "").strip()
                    value = li.get_text(strip=True).replace(f"{key}:", "").strip()
                    control[key] = value
            if control:
                controls.append(control)
        return controls

    @staticmethod
    def controls_to_html_table(controls: list, headers: list) -> str:
        """Convert a list of controls to an HTML table."""
        if not controls:
            return "<p>No controls found in the Markdown content.</p>"

        table_html = "<table id='controls_table'>\n<tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr>\n"
        for control in controls:
            table_html += "<tr>"
            for header in headers:
                table_html += f"<td>{control.get(header, 'N/A')}</td>"
            table_html += "</tr>\n"
        table_html += "</table>"

        return table_html

    @staticmethod
    def generate_history_table(datetime_str: str, controls_info: list, history_table_labels: dict) -> str:
        """
        Generate the HTML content for the history table.

        Args:
            datetime_str (str): Date and time for the revision.
            controls_info (list): List of controls (title and ID).
            history_table_labels (dict): Translated texts for the table headers and content.

        Returns:
            str: Generated HTML content for the history table.
        """
        # Generate HTML for included controls
        included_controls_html = "\n".join(
            f"<li>{control_id} - {control_title}</li>"
            for control_title, control_id in controls_info
        )

        # Build the HTML structure for the history table
        table_html = f"""
        <table id='history_table'>
            <thead>
                <tr>
                    <th>{history_table_labels.get('version', 'Version')}</th>
                    <th>{history_table_labels.get('revised_on', 'Revised On')}</th>
                    <th>{history_table_labels.get('description', 'Description')}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style='width: 16%;'>
                        <p><strong>1.0</strong></p>
                    </td>
                    <td style='width: 21%;'>
                        <p><strong>{datetime_str}</strong></p>
                    </td>
                    <td style='width: 63%; text-align: left;'>
                        <p><strong>{history_table_labels.get('short_description', 'Short Description')}</strong>: {history_table_labels.get('short_description_content', 'Document Created')}</p>
                        <p>&nbsp;</p>
                        <p><strong>{history_table_labels.get('excluded_controls', 'Excluded Controls')}</strong>:</p>
                        <ul>
                            <li>{history_table_labels.get('excluded_controls_content', 'None')}</li>
                        </ul>
                        <p>&nbsp;</p>
                        <p><strong>{history_table_labels.get('included_controls', 'Included Controls')}</strong>:</p>
                        <ul>
                            {included_controls_html}
                        </ul>
                    </td>
                </tr>
            </tbody>
        </table>
        <p>&nbsp;</p>
        """
        return table_html

    @staticmethod
    def generate_html(template_path: str, content_path: str, output_html: str, html_sections: dict, history_table: dict, control_table_labels: dict) -> str:
        """Generate an HTML file from a Markdown file using a template."""
        # Load the template and Markdown content
        template_content = HTMLGenerator.load_template(template_path)
        markdown_content = HTMLGenerator.load_file_content(content_path)

        # Convert Markdown to HTML and extract controls
        html_content = HTMLGenerator.markdown_to_html(markdown_content)
        controls = HTMLGenerator.extract_controls_from_html(html_content)

        # Use control table labels from the configuration
        header_labels = [
            control_table_labels.get("ID", "ID"),
            control_table_labels.get("TITLE", "TITLE"),
            control_table_labels.get("DESCRIPTION", "DESCRIPTION"),
            control_table_labels.get("APPLICABILITY", "APPLICABILITY"),
            control_table_labels.get("SECURITY_RISK", "SECURITY RISK"),
            control_table_labels.get("CRITICALITY", "CRITICALITY"),
            control_table_labels.get("REFERENCES", "REFERENCES")
        ]

        # Generate control and history tables
        controls_table_content = HTMLGenerator.controls_to_html_table(controls, header_labels)
        controls_info = [(c.get(header_labels[0], "N/A"), c.get(header_labels[1], "N/A")) for c in controls]

        datetime_str = datetime.now().strftime("%Y-%m-%d")
        history_table_content = HTMLGenerator.generate_history_table(datetime_str, controls_info, history_table)

        # Render the final HTML using the template
        template = Template(template_content)
        final_html = template.render(
            title="Security Baseline Report",
            control_list_title=html_sections.get("control_list_title", "Security Controls List"),
            controls_table_content=controls_table_content,
            history_table_title=html_sections.get("history_table_title", "Change History"),
            history_table_content=history_table_content
        )

        # Write the final HTML to the output file
        with open(output_html, "w", encoding="utf-8") as file:
            file.write(final_html)

        return final_html
