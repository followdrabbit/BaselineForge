# BaselineForge

**BaselineForge** is a sophisticated application that utilizes **Streamlit** and **OpenAI** to generate AI-enhanced security baselines. It enables users to create organized security controls based on vendor-specific inputs, dynamic prompts, and configuration settings tailored to their preferred language.

## Project Evolution

BaselineForge is the next step in the development of the [Demo-Baseline-Seguranca-IA](https://github.com/followdrabbit/-Demo-Baseline-Seguranca-IA) repository. This new version introduces:
- Enhanced modularity with a dedicated structure for configurations and processing.
- Expanded multi-language support for EN-US, PT-BR, and ES-ES.
- Streamlined user experience with a clean UI and automatic cleanup features.
- Improved integration with OpenAI for generating dynamic security baselines.

## Key Features

- **Multi-language Support**: Supports **EN-US**, **PT-BR**, and **ES-ES**, dynamically loading configurations from `config.toml`:
  - Language-specific labels for vendor, technology, version, category, and baseline generation prompts.
  - Customized table headers for HTML output.
  - Categories for organized and efficient control management.
  
- **Unique ID Generation**: Creates structured, unique IDs using vendor, technology, category, version, and year parameters for consistent tracking and organization.

- **OpenAI Assistant Integration**: Leverages OpenAI’s assistant for generating security controls. Automatically initializes or reuses an assistant configured with context-specific instructions.

- **HTML Conversion**: Consolidates Markdown content into dynamically labeled, language-specific HTML tables for professional reporting.

- **Automated Cleanup**: Cleans up temporary session artifacts to optimize storage usage.

## Project Structure

- **main.py**: The core application script, handling user interface, data processing, and file management.
- **modules/**: Contains modular code for ID generation, OpenAI integration, HTML generation, and configuration loading.
- **config/config.json**: Configuration file for prompts, categories, and other settings.
- **artefacts/**: Temporary storage for session files.
- **templates/template_html.html**: Template for generating HTML reports.

## Getting Started

### Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

### Usage

1. **Select Language**: Choose from **EN-US**, **PT-BR**, or **ES-ES**.
2. **Enter Details**:
   - Select **Vendor** and **Category**.
   - Enter **Technology Name** and **Version** (or "Static" if no version applies).
   - Provide up to **10 URLs**, separated by commas.
3. **Generate Baseline**: A unique ID is created, and URLs are processed into Markdown and HTML formats.
4. **Download**: The final HTML report is available for download, presenting security controls and details.

## TO DO

- [ ] Add dynamic language-specific labels for buttons and progress indicators.
- [ ] Include technology name as a title in the generated document.
- [ ] Integrate logging mechanisms for tracking actions.
- [ ] Add a progress bar for better user experience.
- [ ] Implement a quality check to refine generic controls.

## Acknowledgments

Special thanks to the OpenAI and Streamlit communities for providing the tools and resources that made BaselineForge possible.