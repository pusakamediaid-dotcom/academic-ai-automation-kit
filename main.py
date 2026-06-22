import os
import sys
from core.chunker import chunk_text
from core.summarizer import AcademicSummarizer
from core.insights import InsightExtractor
from core.exporter import Exporter

def main():
    print("--- Academic AI Automation Kit CLI ---")
    token = os.getenv("HF_TOKEN")
    
    try:
        summarizer = AcademicSummarizer(hf_token=token)
        extractor = InsightExtractor(summarizer)
    except Exception as e:
        print(f"Initialization Error: {e}")
        sys.exit(1)

    text = input("\nEnter the academic text to process:\n")
    if not text.strip():
        print("No text provided. Exiting.")
        return

    print("\nSelect Mode:\n1. Short Summary\n2. Detailed Summary\n3. Key Insights\n4. Literature Review Notes")
    choice = input("Choice (1-4): ")
    
    modes = {"1": ("short", "Short Summary"), "2": ("detailed", "Detailed Summary"), "3": ("detailed", "Key Insights"), "4": ("detailed", "Literature Review Notes")}
    
    if choice not in modes:
        print("Invalid choice.")
        return

    mode_key, mode_name = modes[choice]
    
    # Process text (Chunking)
    chunks = chunk_text(text)
    results = []
    
    print("\nProcessing...")
    for i, chunk in enumerate(chunks):
        if choice == "3":
            res = extractor.extract_insights(chunk)
        else:
            res = summarizer.summarize(chunk, mode=mode_key)
        results.append(res)

    final_content = "\n\n".join(results)
    
    # Export
    md_output = Exporter.to_markdown("Research Result", final_content, mode_name)
    json_output = Exporter.to_json("Research Result", final_content, mode_name)
    
    print("\n--- FINAL RESULT ---\n")
    print(final_content)
    print("\n--- MARKDOWN EXPORT ---\n")
    print(md_output)
    
    # Save to files
    with open("output_summary.md", "w") as f: f.write(md_output)
    with open("output_summary.json", "w") as f: f.write(json_output)
    print("\nResults saved to output_summary.md and output_summary.json")

if __name__ == "__main__":
    main()
