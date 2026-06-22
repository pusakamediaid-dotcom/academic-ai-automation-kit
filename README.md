# Academic AI Automation Kit 🎓

The **Academic AI Automation Kit** is a professional-grade toolkit designed for researchers, students, and academics to streamline the process of reading, summarizing, and synthesizing complex academic literature. 

Instead of reading every word of a 30-page paper, use this kit to extract the core thesis, methodology, and findings in seconds.

## 🚀 Features
- **Smart Chunking**: Automatically handles long texts that exceed AI model limits.
- **Multi-Mode Processing**: 
  - `Short Summary`: For quick scanning.
  - `Detailed Summary`: For deep understanding.
  - `Key Insights`: Focuses on the "aha!" moments and conclusions.
  - `Literature Review Notes`: Structured for direct insertion into a research vault.
- **Flexible Interfaces**: Run it via Command Line, a web-based Gradio UI, or Google Colab.
- **Structured Output**: Export results as Markdown (perfect for Notion/Obsidian) or JSON (for developers).

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
Open the provided local URL in your browser.

### 3. Run via CLI
```bash
python main.py
```

### 4. Google Colab (Zero Setup)
Open the notebook in `notebooks/Academic_AI_Automation_Kit_Colab.ipynb` and run all cells.

## ⚠️ Limitations & Disclaimer
- **AI Hallucinations**: This tool uses Large Language Models. Always verify critical facts, citations, and data against the original source.
- **Context Window**: While we use chunking, extremely long documents may lose some global context between chunks.
- **Academic Integrity**: This tool is intended to *assist* in understanding and organizing research, not to replace original reading or to automate the writing of academic papers (which may violate institutional policies).

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
