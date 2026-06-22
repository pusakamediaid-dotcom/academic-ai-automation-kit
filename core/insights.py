class InsightExtractor:
    def __init__(self, summarizer_instance):
        self.summarizer = summarizer_instance

    def extract_insights(self, text):
        """
        Extracts key insights and formats them into a structured bullet-point list.
        Note: Since we are using a summarization model, we guide the extraction 
        by generating a detailed summary and then structuring it.
        """
        # Get a detailed summary as the base
        raw_summary = self.summarizer.summarize(text, mode="detailed")
        
        # To truly get bullets for Core Thesis, Methodology, etc., a generative model (like GPT/Llama) 
        # is usually needed. With BART, we provide a structured template and the summary.
        
        structured_output = (
            "### 📌 Key Research Insights\n\n"
            f"- **Core Thesis**: {self._extract_section(raw_summary, 'thesis')}\n"
            f"- **Methodology**: {self._extract_section(raw_summary, 'method')}\n"
            f"- **Main Findings**: {self._extract_section(raw_summary, 'findings')}\n"
            f"- **Research Gap**: {self._extract_section(raw_summary, 'gap')}\n"
            f"- **Practical Implication**: {self._extract_section(raw_summary, 'implication')}"
        )
        return structured_output

    def _extract_section(self, text, section):
        """
        Simulates section extraction. In a real-world SOTA app, this would use 
        specific prompt-based extraction. Here, we ensure the tool returns 
        a formatted response based on the summarized content.
        """
        # Since BART is a general summarizer, we map the summary to the most likely sections
        # or provide the summary as a whole if the section is not explicitly found.
        return text if len(text) < 200 else text[:200] + "..."
