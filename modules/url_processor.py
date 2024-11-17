import os
import requests
import html2text
import uuid


class URLProcessor:
    """Handles URL fetching and saving as Markdown."""

    def __init__(self, artifacts_dir):
        """
        Initializes the URLProcessor with the specified artifacts directory.

        Args:
            artifacts_dir (str): Directory where artifacts (Markdown files) will be saved.
        """
        self.artifacts_dir = artifacts_dir
        os.makedirs(self.artifacts_dir, exist_ok=True)

    def fetch_page_content(self, url):
        """
        Fetches the content of a given URL.

        Args:
            url (str): The URL to fetch content from.

        Returns:
            str: The HTML content of the page, or None if an error occurs.
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from URL '{url}': {e}")
            return None

    def save_as_markdown(self, url, html_content, section_id):
        """
        Saves HTML content as a Markdown file in the specified artifacts directory.

        Args:
            url (str): The URL being processed.
            html_content (str): The HTML content fetched from the URL.
            section_id (str): Unique identifier for the session.

        Returns:
            str: Path to the saved Markdown file.
        """
        try:
            # Generate a unique and safe filename based on the URL
            sanitized_url = url.replace("https://", "").replace("http://", "").replace("/", "_").replace("?", "_").replace("&", "_")
            unique_filename = f"{sanitized_url}_{section_id}.md"
            markdown_file = os.path.join(self.artifacts_dir, unique_filename)

            # Convert HTML to Markdown
            converter = html2text.HTML2Text()
            converter.ignore_links = False
            markdown_content = converter.handle(html_content)

            # Add a header with reference information
            header = f"# Processed Content from URL: {{'REFERENCE': '{url}'}}\n\n{markdown_content}"

            # Save the Markdown content
            with open(markdown_file, "w", encoding="utf-8") as file:
                file.write(header)

            print(f"Markdown file saved: {markdown_file}")
            return markdown_file
        except Exception as e:
            raise FileNotFoundError(f"Failed to save Markdown file for URL '{url}': {e}")

    def generate_unique_id(self):
        """
        Generates a unique identifier for the session.

        Returns:
            str: A unique UUID.
        """
        return str(uuid.uuid4())
