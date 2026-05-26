"""
Sanitized pipeline pseudocode.

This file is not production code.
It only demonstrates the high-level idea of the document processing flow.
No proprietary logic, client data or internal configuration is included.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class PipelineResult:
    text: str
    nlp_metadata: dict[str, Any]
    llm_metadata: dict[str, Any]
    classification: dict[str, Any]
    final_output: dict[str, Any]


def detect_file_type(file_path: str) -> str:
    """Detect document type."""
    return "pdf_or_image"


def extract_text(file_path: str) -> str:
    """Extract text directly or through OCR when needed."""
    file_type = detect_file_type(file_path)

    if file_type == "image_or_scanned_pdf":
        return run_ocr(file_path)

    return read_machine_text(file_path)


def run_ocr(file_path: str) -> str:
    """Run OCR on scanned or image-based documents."""
    return "synthetic OCR text"


def read_machine_text(file_path: str) -> str:
    """Read text from a machine-readable document."""
    return "synthetic readable text"


def extract_metadata_with_nlp(text: str) -> dict[str, Any]:
    """Extract metadata using deterministic NLP rules and validators."""
    return {
        "case_number": "CASE-2025-001",
        "document_date": "2025-01-15",
        "confidence": 0.88,
    }


def extract_metadata_with_llm(text: str) -> dict[str, Any]:
    """Extract and validate metadata using an LLM-assisted flow."""
    return {
        "case_number": "CASE-2025-001",
        "document_date": "2025-01-15",
        "confidence": 0.93,
    }


def classify_document_semantically(text: str) -> dict[str, Any]:
    """Classify a document using semantic similarity against category definitions."""
    return {
        "category_code": "DEMO-STATUS-REQUEST",
        "category_name": "Case status request",
        "confidence": 0.91,
    }


def orchestrate_decision(
    nlp_metadata: dict[str, Any],
    llm_metadata: dict[str, Any],
    classification: dict[str, Any],
) -> dict[str, Any]:
    """Select final values based on agreement, confidence and validation rules."""
    final_case_number = (
        nlp_metadata["case_number"]
        if nlp_metadata["case_number"] == llm_metadata["case_number"]
        else llm_metadata["case_number"]
    )

    return {
        "document_metadata": {
            "case_number": final_case_number,
            "document_date": llm_metadata["document_date"],
        },
        "classification": classification,
        "decision_orchestrator": {
            "selected_source": "hybrid",
            "reasoning_summary": "Final values selected after comparing NLP and LLM outputs.",
            "requires_manual_review": False,
        },
    }


def process_document(file_path: str) -> PipelineResult:
    """Run the full sanitized processing flow."""
    text = extract_text(file_path)
    nlp_metadata = extract_metadata_with_nlp(text)
    llm_metadata = extract_metadata_with_llm(text)
    classification = classify_document_semantically(text)
    final_output = orchestrate_decision(nlp_metadata, llm_metadata, classification)

    return PipelineResult(
        text=text,
        nlp_metadata=nlp_metadata,
        llm_metadata=llm_metadata,
        classification=classification,
        final_output=final_output,
    )


if __name__ == "__main__":
    result = process_document("examples/sample-document.txt")
    print(result.final_output)
