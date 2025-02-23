# BaselineForge

**BaselineForge** is a sophisticated application that utilizes **Streamlit** and **OpenAI** to generate AI-enhanced security baselines. It enables users to create structured security controls based on vendor-specific inputs, dynamic prompts, and configuration settings tailored to their preferred language.

**Note:** This version is currently functional only for AWS products and in the EN-US language.

## Project Evolution

BaselineForge is an evolution of the [Demo-Baseline-Seguranca-IA](https://github.com/followdrabbit/-Demo-Baseline-Seguranca-IA) repository. This updated version introduces:

- Enhanced modularity with dedicated modules for configuration, data processing, and report generation.
- Multi-language support planned for **EN-US**, **PT-BR**, and **ES-ES**, but currently only **EN-US** is functional.
- Automated security control generation powered by OpenAI.
- HTML report generation with structured tables and historical change tracking.
- Streamlined artifact management with automatic cleanup of session files.

## Key Features

- **Multi-language Support (Planned)**: While support for **PT-BR** and **ES-ES** is being developed, the current functional implementation is limited to **EN-US**.

- **Unique ID Generation**: Uses `IDGenerator` to create structured, unique IDs using vendor, technology, version, and year parameters.

- **OpenAI Assistant Integration**: Leverages OpenAI’s assistant for security control generation. Automates multiple AI-driven processing steps:

  - `Requisitor`: Extracts security-relevant content.
  - `ControlGen`: Generates security controls per document.
  - `ControlRefiner`: Unifies and refines controls.
  - `RiskEvaluator`: Assesses security risks.

- **HTML Report Generation**: Converts Markdown content into structured, professional HTML reports using `HTMLGenerator`.

- **Automated Cleanup**: Session artifacts are removed post-processing using `cleanup_util`.

## Project Structure

```
BaselineForge/
│── main.py               # Main Streamlit application
│── modules/
│   ├── config_loader.py   # Handles configuration management
│   ├── url_processor.py   # Fetches and processes webpage content
│   ├── id_generator.py    # Generates unique control IDs
│   ├── openai_service.py  # Handles OpenAI API interaction
│   ├── html_generator.py  # Generates HTML reports
│   ├── agent_processor.py # Processes security controls with OpenAI
│   ├── data_importer.py   # Converts Markdown files into structured data
│   ├── cleanup_util.py    # Manages session cleanup
│── config/config.json     # Configuration file for UI elements and prompts
│── artefacts/             # Temporary session storage
│── templates/
│   ├── template_html.html # HTML template for reports
```

## Installation

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:

   ```bash
   streamlit run main.py
   ```

## Usage

1. **Select Language**: Currently only **EN-US** is functional. 
2. **Enter Details**:
   - Select **Vendor**.
   - Enter **Technology Name**.
   - Provide up to **10 URLs**, separated by commas.
3. **Generate Baseline**: The pipeline will execute, processing URLs and generating structured security controls.
4. **Download Report**: The final HTML report will be available for download.

## To Do

- [ ] Implement functional support for **PT-BR** and **ES-ES**.
- [ ] Enhance AI processing pipeline with additional security evaluations.
- [ ] Enhance logging for debugging and performance tracking.
- [ ] Add dynamic language-specific UI enhancements.
- [ ] Improve the user experience with a progress bar.

## Acknowledgments

Special thanks to the OpenAI and Streamlit communities for providing the tools and resources that made BaselineForge possible.

