---
name: testing
description: Guidelines for testing the Agnara Task Intelligence application.
---

# Testing Guidelines

## Mandatory Tests
- **Positive Validation (Low Risk)**: Verify that a task with no high-risk keywords produces `complexity=low`, `risk=low`, and `requires_review=False`.
- **Positive Validation (High Risk)**: Verify that a task with keywords like "oauth", "database", "security" produces `complexity=high`, `risk=high`, and `requires_review=True`.
- **Negative Validation**: Verify that passing invalid input types (e.g., `{"task": 12345}`) results in a canonical `Failure` with `code="invalid_input"`.
- **Metadata**: Verify that the capability metadata (ID, description, scopes, risk) is correctly compiled.

## Commands
Before finalizing any work, you MUST run:
```bash
python -m pytest tests/ -v
ruff check .
ruff format --check .
```

## Completion Criteria
Do not consider a task complete until all quality gates pass on Python 3.14.
