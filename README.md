# Academic AI Automation Kit — Research Automation OS

Turn academic PDFs or pasted text into professional summaries, structured insights, Notion research pages, and PDF reports automatically.

## 🚀 What it Does
The Research Automation OS is a high-performance pipeline that replaces manual research skimming. It extracts text from PDFs, processes it using SOTA Transformers, and syncs the results directly to your knowledge management system.

### The Pipeline:
`PDF/Text` $\rightarrow$ `Clean & Chunk` $\rightarrow$ `AI Summarization` $\rightarrow$ `Insight Extraction` $\rightarrow$ `Notion Sync` $\rightarrow$ `PDF Report`

## 🛠️ Feature Table
| Feature | Description | Integration |
| :--- | :--- | :--- |
| **Auto PDF Reader** | Extracts and cleans text from academic PDFs. | `pypdf` |
| **AI Engine** | Detailed summaries and structured insights. | `Hugging Face` |
| **Research Vault** | Automatic sync to a structured Notion database. | `Notion API` |
| **Report Gen** | One-click professional PDF report generation. | `PDFMonkey` |
| **Multi-Interface** | Use via Web UI, CLI, or Google Colab. | `Gradio` |

## 🏁 Quickstart

### Option A: Google Colab (Fastest)
1. Open `notebooks/Academic_AI_Automation_Kit_Colab.ipynb`.
2. Run all cells.
3. Open the Gradio link and upload your PDF.

### Option B: Local Installation
1. `git clone https://github.com/pusakamediaid-dotcom/academic-ai-automation-kit.git`
2. `pip install -r requirements.txt`
3. `python app.py`

## 🔑 Environment Variables
Create a `.env` file based on `.env.example`:
- `HF_TOKEN`: Your Hugging Face token.
- `NOTION_API_KEY`: Your Notion internal integration token.
- `NOTION_DATABASE_ID`: The ID of your research database.
- `PDFMONKEY_API_KEY`: Your PDFMonkey API key.
- `PDFMONKEY_TEMPLATE_ID`: Your report template ID.

## 📖 Setup Guides
- **Notion**: See `docs/NOTION_SETUP.md`
- **PDFMonkey**: See `docs/PDFMONKEY_SETUP.md`
- **HF**: See `docs/HUGGINGFACE_SETUP.md`

## ⚠️ Limitations & Integrity
- **Verification**: AI can hallucinate. Always cross-reference the generated summaries with the original paper.
- **PDF Complexity**: Multi-column PDFs or scanned images (OCR) may require manual text cleaning.
- **Academic Integrity**: This tool is a research *assistant*. It should not be used to bypass the critical reading process.
