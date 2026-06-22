# Academic AI Automation Kit 🎓

The **Academic AI Automation Kit** is a tool designed for researchers and students to streamline the process of reading and synthesizing academic literature. 

Instead of reading every word of a long paper, use this kit to extract the core thesis and findings more efficiently.

## 🚀 Features
- **Paragraph-Aware Chunking**: Handles long texts by splitting them at natural breaks (paragraphs/sentences).
- **Multi-Mode Processing**: 
  - `Short Summary`: For quick scanning.
  - `Detailed Summary`: For deeper understanding.
  - `Key Insights`: Structured bullet points (Thesis, Methodology, Findings, etc.).
  - `Literature Review Notes`: Formatted for research databases.
- **Flexible Interfaces**: Run it via Command Line, a web-based Gradio UI, or Google Colab.
- **Structured Output**: Export results as Markdown or JSON.

## 🛠️ Quickstart

### 1. Local Installation
```bash
git clone https://github.com/pusakamediaid-dotcom/academic-ai-automation-kit.git
cd academic-ai-automation-kit
pip install -r requirements.txt
```

### 2. Run the Web UI (Recommended)
```bash
python app.py
```

### 3. Google Colab (Zero Setup)
Open the notebook in `notebooks/Academic_AI_Automation_Kit_Colab.ipynb` and run all cells.

## ⚠️ Limitations & Disclaimer
- **AI Hallucinations**: Always verify critical facts and citations against the original source.
- **Text-Based**: This tool processes pasted text. It does not currently support direct PDF uploads.
- **Academic Integrity**: Intended as a research assistant, not a replacement for critical reading.

## 📜 License
Distributed under the MIT License.
