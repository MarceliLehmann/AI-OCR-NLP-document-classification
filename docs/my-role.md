# My Role

This document describes my contribution to the AI document processing project in a safe and sanitized way.

No proprietary code, client-specific data or confidential infrastructure details are included.

---

## Area of Work

I worked on a commercial AI document processing pipeline focused on OCR, metadata extraction, semantic classification and LLM-assisted validation.

My responsibilities were connected with both implementation and system organization.

---

## Main Contributions

### OCR and Document Processing

I worked with document input handling and OCR-oriented processing flow.

The goal was to prepare document text for later metadata extraction and classification.

---

### Metadata Extraction

I contributed to logic for extracting structured information from unstructured administrative documents.

This included fields such as:

- document identifiers,
- dates,
- sender and recipient information,
- case-related metadata,
- organizational routing information.

---

### Semantic Classification

I worked on classification logic based on semantic matching.

The idea was to compare document text with predefined category definitions and select the most relevant target class.

---

### LLM-Based Validation

I helped design a flow where an LLM independently analyzed the document and produced an alternative structured result.

This result could then be compared with traditional extraction output.

---

### Decision Orchestration

One of the key ideas was to use an orchestrator that compared multiple candidate outputs and selected the best final value for each metadata field.

This helped reduce errors caused by relying on only one extraction method.

---

### Code Organization and Workflow Design

I also worked on improving the structure of the project, including:

- modularizing the processing flow,
- separating responsibilities between components,
- improving readability,
- preparing the project for testing and orchestration.

---

## Skills Used

- Python
- OCR processing
- NLP
- embeddings
- semantic search
- LLM prompting and validation
- JSON output design
- workflow orchestration
- testing
- documentation
- debugging AI pipeline behavior

---

## Result

The work improved my practical understanding of how to build AI systems that combine traditional extraction methods with LLM-based reasoning.

The project also gave me experience in working with real-world document complexity, where input data can be incomplete, inconsistent or difficult to parse.
