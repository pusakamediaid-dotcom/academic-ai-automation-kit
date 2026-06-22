import os
from transformers import pipeline

class AcademicSummarizer:
    def __init__(self, hf_token=None):
        self.token = hf_token or os.getenv("HF_TOKEN")
        self.model_name = "facebook/bart-large-cnn"
        try:
            self.summarizer = pipeline("summarization", model=self.model_name, token=self.token)
        except Exception as e:
            print(f"Warning: Failed to load model with token. Trying public access... Error: {e}")
            try:
                self.summarizer = pipeline("summarization", model=self.model_name)
            except Exception as e2:
                raise RuntimeError(f"Critical Error: Could not load AI model. {e2}")

    def summarize(self, text, mode="short"):
        """Summarizes text based on the requested mode."""
        # BART limits are around 1024 tokens. 
        # We assume the text is already chunked or short enough.
        
        if mode == "short":
            max_l, min_l = 60, 30
        elif mode == "detailed":
            max_l, min_l = 150, 80
        else: # Literature review mode
            max_l, min_l = 200, 100
            
        try:
            summary = self.summarizer(text, max_length=max_l, min_length=min_l, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Error during summarization: {str(e)}"
