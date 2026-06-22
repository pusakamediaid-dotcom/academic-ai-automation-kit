import gradio as gr
import os
from core.chunker import chunk_text
from core.summarizer import AcademicSummarizer
from core.insights import InsightExtractor
from core.exporter import Exporter

def process_ai(text, mode):
    if not text.strip():
        return "Please enter some text.", ""
    
    token = os.getenv("HF_TOKEN")
    try:
        summarizer = AcademicSummarizer(hf_token=token)
        extractor = InsightExtractor(summarizer)
    except Exception as e:
        return f"Error loading AI model: {e}", ""

    # Chunking
    chunks = chunk_text(text)
    results = []
    
    mode_map = {
        "Short Summary": ("short", False),
        "Detailed Summary": ("detailed", False),
        "Key Insights": ("detailed", True),
        "Literature Review Notes": ("detailed", False)
    }
    
    mode_key, is_insight = mode_map[mode]
    
    for chunk in chunks:
        if is_insight:
            res = extractor.extract_insights(chunk)
        else:
            res = summarizer.summarize(chunk, mode=mode_key)
        results.append(res)
    
    final_text = "\n\n".join(results)
    markdown = Exporter.to_markdown("Research Result", final_text, mode)
    json_res = Exporter.to_json("Research Result", final_text, mode)
    
    return markdown, json_res

# Gradio Interface
with gr.Blocks(title="Academic AI Automation Kit") as demo:
    gr.Markdown("# 🎓 Academic AI Automation Kit")
    gr.Markdown("Transform long academic papers into structured summaries and insights using SOTA AI models.")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Academic Text", lines=10, placeholder="Paste your paper abstract or section here...")
            mode_dropdown = gr.Dropdown(
                choices=["Short Summary", "Detailed Summary", "Key Insights", "Literature Review Notes"], 
                value="Short Summary", 
                label="Processing Mode"
            )
            submit_btn = gr.Button("Process Text", variant="primary")
        
        with gr.Column():
            output_md = gr.Markdown(label="Markdown Result")
            output_json = gr.Code(label="JSON Result", language="json")
            
    submit_btn.click(fn=process_ai, inputs=[input_text, mode_dropdown], outputs=[output_md, output_json])

if __name__ == "__main__":
    demo.launch()
