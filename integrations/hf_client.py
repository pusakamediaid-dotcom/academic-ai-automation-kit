import os
from transformers import pipeline

class HFClient:
    def __init__(self):
        self.token = os.getenv("HF_TOKEN")
        self.model_name = os.getenv("HF_MODEL_NAME", "facebook/bart-large-cnn")
        self._pipeline = None

    def load_summarization_pipeline(self):
        """Loads the pipeline once (Singleton)."""
        if self._pipeline is None:
            try:
                print(f"Loading AI Model: {self.model_name}...")
                self._pipeline = pipeline(
                    "summarization", 
                    model=self.model_name, 
                    token=self.token
                )
                print("Model loaded successfully.")
            except Exception as e:
                print(f"Error loading model with token: {e}. Trying public access...")
                try:
                    self._pipeline = pipeline("summarization", model=self.model_name)
                except Exception as e2:
                    raise RuntimeError(f"Critical Failure: AI model could not be loaded. {e2}")
        return self._pipeline

    def summarize_chunk(self, chunk: str, mode: str) -> str:
        pipeline = self.load_summarization_pipeline()
        
        # Mode settings
        if mode == "short":
            max_l, min_l = 60, 30
        elif mode == "detailed":
            max_l, min_l = 150, 80
        else: # Review notes
            max_l, min_l = 200, 100
            
        try:
            summary = pipeline(chunk, max_length=max_l, min_length=min_l, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Summarization error: {str(e)}"

    def summarize_chunks(self, chunks: list[str], mode: str) -> str:
        results = [self.summarize_chunk(chunk, mode) for chunk in chunks]
        return "\n\n".join(results)

    def detect_model_status(self) -> dict:
        return {
            "status": "ready" if self._pipeline else "not_loaded",
            "model": self.model_name,
            "token_used": bool(self.token)
        }
