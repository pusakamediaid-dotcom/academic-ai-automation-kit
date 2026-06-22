import os
from transformers import pipeline

class AcademicResearchToolkit:
    def __init__(self, hf_token=None):
        self.hf_token = hf_token
        # Initialize summarization pipeline
        print("Loading AI Models... Please wait.")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", token=hf_token)
        # Initialize keyword extraction (using a simple approach or a dedicated model)
        self.extractor = pipeline("feature-extraction", model="distilbert-base-uncased", token=hf_token)

    def summarize_text(self, text, max_len=130, min_len=30):
        """Summarizes a long academic text into a concise paragraph."""
        try:
            summary = self.summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Error in summarization: {str(e)}"

    def extract_key_insights(self, text):
        """Simplified insight extraction: picks the most representative sentences."""
        # In a real scenario, this would use a more complex NLP approach
        # For this toolkit, we provide a high-quality summary as the primary insight
        return self.summarize_text(text, max_len=150, min_len=50)

if __name__ == "__main__":
    # Replace 'YOUR_HF_TOKEN' with your actual token or set it as environment variable
    TOKEN = os.getenv("HF_TOKEN", "YOUR_HF_TOKEN")
    toolkit = AcademicResearchToolkit(hf_token=TOKEN)

    print("\n--- Academic AI Toolkit ---")
    print("1. Summarize Academic Text")
    print("2. Extract Key Insights")
    
    choice = input("\nSelect an option (1/2): ")
    
    if choice == '1' or choice == '2':
        text_to_process = input("\nPaste the text from the academic paper here:\n")
        if choice == '1':
            print("\nGenerating Summary...\n")
            print(toolkit.summarize_text(text_to_process))
        else:
            print("\nExtracting Key Insights...\n")
            print(toolkit.extract_key_insights(text_to_process))
    else:
        print("Invalid choice.")
