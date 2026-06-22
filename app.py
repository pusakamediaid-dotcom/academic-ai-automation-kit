import gradio as gr
import os
from core.pdf_reader import extract_text_from_pdf_bytes, clean_extracted_text
from core.research_pipeline import ResearchPipeline
from integrations.notion_client import NotionClient
from integrations.pdfmonkey_client import PDFMonkeyClient

# Init Pipeline & Clients
pipeline = ResearchPipeline()
notion = NotionClient()
pdfmonkey = PDFMonkeyClient()

def process_research_paper(pdf_file, text_input, mode, sync_notion, gen_pdf):
    # 1. Text Extraction
    source_type = "text"
    raw_text = ""
    
    if pdf_file is not None:
        source_type = "pdf"
        try:
            # Read bytes from the Gradio file path
            with open(pdf_file.name, "rb") as f:
                raw_text = extract_text_from_pdf_bytes(f.read())
        except Exception as e:
            return f"PDF Error: {e}", "", "❌", "❌", "", ""
    elif text_input and text_input.strip():
        raw_text = text_input
    else:
        return "Error: Please provide either a PDF or pasted text.", "", "❌", "❌", "", ""

    cleaned_text = clean_extracted_text(raw_text)
    
    # 2. AI Pipeline
    try:
        report = pipeline.run(cleaned_text, source_type, mode=mode)
    except Exception as e:
        return f"AI Pipeline Error: {e}", "", "❌", "❌", "", ""

    # 3. Notion Sync
    notion_status = "Skipped"
    notion_url = ""
    if sync_notion:
        res = notion.sync_to_notion_database(report)
        if res["ok"]:
            notion_status = "✅ Synced"
            notion_url = res.get("url", "")
        else:
            notion_status = f"❌ {res['message']}"

    # 4. PDF Report
    pdf_status = "Skipped"
    pdf_url = ""
    if gen_pdf:
        res = pdfmonkey.generate_pdf_report(report)
        if res["ok"]:
            pdf_status = "✅ Generated"
            pdf_url = pdfmonkey.get_download_url(res.get("document_id", ""))
        else:
            pdf_status = f"❌ {res['message']}"

    return (
        report["markdown_report"], 
        report["json_report"], 
        notion_status, 
        notion_url, 
        pdf_status, 
        pdf_url
    )

# UI Layout
with gr.Blocks(title="Academic Research Automation OS") as demo:
    gr.Markdown("# 🎓 Academic Research Automation OS")
    gr.Markdown("The professional pipeline for transforming academic PDFs into structured research vaults.")
    
    with gr.Row():
        with gr.Column():
            pdf_upload = gr.File(label="Upload Academic PDF", file_types=[".pdf"])
            text_input = gr.Textbox(label="Or Paste Text", lines=8, placeholder="Paste paper text here...")
            mode_dropdown = gr.Dropdown(
                choices=["Short Summary", "Detailed Summary", "Key Insights", "Literature Review Notes"], 
                value="Detailed Summary", 
                label="AI Processing Mode"
            )
            with gr.Row():
                sync_notion = gr.Checkbox(label="Sync to Notion")
                gen_pdf = gr.Checkbox(label="Generate PDF Report")
            
            submit_btn = gr.Button("🚀 Process Research Paper", variant="primary")
        
        with gr.Column():
            output_md = gr.Markdown(label="AI Analysis Result")
            output_json = gr.Code(label="JSON Data", language="json")
            with gr.Row():
                notion_status = gr.Textbox(label="Notion Status", interactive=False)
                pdf_status = gr.Textbox(label="PDF Report Status", interactive=False)
            notion_url = gr.Textbox(label="Notion Page URL", interactive=False)
            pdf_url = gr.Textbox(label="PDF Download URL", interactive=False)
            
    submit_btn.click(
        fn=process_research_paper, 
        inputs=[pdf_upload, text_input, mode_dropdown, sync_notion, gen_pdf], 
        outputs=[output_md, output_json, notion_status, notion_url, pdf_status, pdf_url]
    )

if __name__ == "__main__":
    demo.launch()
