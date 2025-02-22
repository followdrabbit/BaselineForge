import os
import requests
import html2text


class URLProcessor:
    """Handles URL fetching and saving as Markdown."""

    def __init__(self, artifacts_dir, session_id):
        """
        Initializes the URLProcessor with the specified artifacts directory and session ID.

        Args:
            artifacts_dir (str): Directory where artifacts (Markdown files) will be saved.
            session_id (str): Unique session identifier to ensure consistency.
        """
        self.artifacts_dir = artifacts_dir
        self.session_id = session_id

    def fetch_page_content(self, url):
        """
        Fetches the content of a given URL.

        Args:
            url (str): The URL to fetch content from.

        Returns:
            str: The HTML content of the page, or None if an error occurs.
        """
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            )
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from URL '{url}': {e}")
            return None

    def save_as_markdown(self, url, html_content):
        """
        Saves HTML content as a Markdown file using the stored session ID.

        Args:
            url (str): The URL being processed.
            html_content (str): The HTML content fetched from the URL.

        Returns:
            str: Path to the saved Markdown file.
        """
        try:
            # Generate a unique and safe filename based on the URL
            sanitized_url = (
                url.replace("https://", "")
                .replace("http://", "")
                .replace("/", "_")
                .replace("?", "_")
                .replace("&", "_")
            )
            unique_filename = f"{sanitized_url}_{self.session_id}.md"
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
