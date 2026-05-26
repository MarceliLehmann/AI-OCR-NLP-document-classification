# Testing and Quality

This document describes the general testing and quality approach used in the sanitized portfolio version of the project.

---

## Testing Goals

The main goal of testing was to make the document processing pipeline more reliable and easier to maintain.

The system had to handle many edge cases, including:

- missing fields,
- poor OCR quality,
- different document layouts,
- inconsistent formatting,
- ambiguous metadata,
- classification uncertainty.

---

## Types of Tests

### Unit Tests

Unit tests were used for isolated logic such as:

- field extraction,
- validation helpers,
- classification utilities,
- JSON normalization,
- decision rules.

---

### Integration Tests

Integration tests were useful for checking whether multiple pipeline stages worked together correctly.

Example integration areas:

- file input -> text extraction,
- OCR output -> metadata extraction,
- NLP result -> decision orchestrator,
- final output -> JSON validation.

---

### Synthetic Test Data

For public portfolio purposes, only synthetic examples should be used.

Real documents, client data or internal test samples should not be uploaded to a public repository.

---

## Quality Practices

Useful quality practices for this type of project include:

- clear module boundaries,
- deterministic output schemas,
- validation of extracted fields,
- logging without exposing sensitive data,
- synthetic regression examples,
- code formatting and linting,
- documented configuration.

---

## Important Public Repository Rule

A public portfolio repository should never include:

- real documents,
- production logs,
- internal configuration,
- private package registry URLs,
- credentials,
- client-specific test files,
- embeddings generated from confidential data.
