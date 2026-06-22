import argparse
import os
from core.pdf_reader import extract_text_from_pdf, clean_extracted_text
from core.research_pipeline import ResearchPipeline
from integrations.notion_client import NotionClient
from integrations.pdfmonkey_client import PDFMonkeyClient

def main():
    parser = argparse.ArgumentParser(description="Academic Research Automation OS CLI")
    parser.add_argument("--pdf", type=str, help="Path to academic PDF file")
    parser.add_argument("--text", type=str, help="Academic text to process")
    parser.add_argument("--mode", type=str, default="detailed", help="Mode: short, detailed, review")
    parser.add_argument("--sync-notion", action="store_true", help="Sync result to Notion")
    parser.add_argument("--generate-pdf", action="store_true", help="Generate PDF report via PDFMonkey")
    
    args = parser.parse_args()
    
    # 1. Extraction
    source_type = "text"
    raw_text = ""
    
    if args.pdf:
        source_type = "pdf"
        raw_text = extract_text_from_pdf(args.pdf)
    elif args.text:
        raw_text = args.text
    else:
        print("Error: Please provide either --pdf or --text")
        return

    cleaned_text = clean_extracted_text(raw_text)
    
    # 2. Pipeline
    pipeline = ResearchPipeline()
    try:
        report = pipeline.run(cleaned_text, source_type, mode=args.mode)
    except Exception as e:
        print(f"Pipeline Error: {e}")
        return

    # 3. Integrations
    if args.sync_notion:
        notion = NotionClient()
        res = notion.sync_to_notion_database(report)
        print(f"Notion Sync: {res['message'] if not res['ok'] else 'Success! URL: ' + res['url']}")
        
    if args.generate_pdf:
        pdfm = PDFMonkeyClient()
        res = pdfm.generate_pdf_report(report)
        print(f"PDF Report: {res['message'] if not res['ok'] else 'Success! ID: ' + res['document_id']}")

    # 4. Output
    print("\n--- Research Report ---\n")
    print(report["markdown_report"])
    
    # Save to file
    with open("research_report.md", "w") as f:
        f.write(report["markdown_report"])
    print("\nReport saved to research_report.md")

if __name__ == "__main__":
    main()
