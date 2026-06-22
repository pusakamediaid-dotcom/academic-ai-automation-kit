class InsightExtractor:
    def __init__(self, summarizer_instance):
        self.summarizer = summarizer_instance

    def extract_insights(self, text):
        """Extracts key insights by leveraging the summarizer for a 'detailed' view."""
        # In a professional tool, we might use a different model or prompt.
        # Here we use the high-detail summarization as the proxy for insights.
        return self.summarizer.summarize(text, mode="detailed")
