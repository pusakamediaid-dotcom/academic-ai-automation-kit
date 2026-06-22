import os
import requests

class PDFMonkeyClient:
    def __init__(self):
        self.api_key = os.getenv("PDFMONKEY_API_KEY")
        self.template_id = os.getenv("PDFMONKEY_TEMPLATE_ID")
        self.endpoint = "https://api.pdfmonkey.io/api/v1/documents"

    def is_pdfmonkey_configured(self) -> bool:
        return bool(self.api_key and self.template_id)

    def build_pdfmonkey_payload(self, report_data: dict) -> dict:
        """Maps report data to PDFMonkey dynamic data."""
        return {
            "template_id": self.template_id,
            "payload": {
                "title": report_data.get("title", "Research Report"),
                "summary_short": report_data.get("summary_short", ""),
                "summary_detailed": report_data.get("summary_detailed", ""),
                "core_thesis": report_data["key_insights"].get("core_thesis", ""),
                "methodology": report_data["key_insights"].get("methodology", ""),
                "main_findings": report_data["key_insights"].get("main_findings", ""),
                "research_gap": report_data["key_insights"].get("research_gap", ""),
                "practical_implication": report_data["key_insights"].get("practical_implication", ""),
                "literature_review_notes": report_data.get("literature_review_notes", ""),
                "processed_at": report_data["metadata"].get("processed_at", ""),
                "model": report_data["metadata"].get("model", "")
            }
        }

    def generate_pdf_report(self, report_data: dict) -> dict:
        if not self.is_pdfmonkey_configured():
            return {"ok": False, "configured": False, "message": "PDFMonkey not configured."}
        
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = self.build_pdfmonkey_payload(report_data)
        
        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            if response.status_code == 201:
                data = response.json()
                # PDFMonkey returns a document object with an ID
                document_id = data.get("document", {}).get("id")
                return {"ok": True, "configured": True, "document_id": document_id, "status": "Generating"}
            else:
                return {"ok": False, "configured": True, "message": response.text}
        except Exception as e:
            return {"ok": False, "configured": True, "message": str(e)}

    def get_download_url(self, document_id: str) -> str:
        """Returns the public download URL if available."""
        # Simplified: normally we would poll the status.
        return f"https://api.pdfmonkey.io/api/v1/documents/{document_id}/download"
