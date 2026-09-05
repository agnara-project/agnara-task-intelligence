# Capabilities

This document lists the capabilities exposed by the Agnara Task Intelligence application.

## 1. `task_intelligence.analyze_task`

**Purpose**: Analyzes a software development task and estimates its complexity, risk, and whether it requires human review.

### Metadata
- **ID**: `task_intelligence.analyze_task`
- **Scopes**: `["tasks:analyze"]`
- **Operational Risk**: `LOW` (This is the risk of executing the capability itself, not the risk of the task being analyzed)
- **Idempotent**: `True`

> **Note on Risk**: The `Risk` defined in the capability metadata (`Risk.LOW`) represents the *operational risk* of running the capability. The `TaskAnalysis.risk` output represents the *domain risk* of the software task being analyzed. They are different concepts.

### Input
- **task** (`str`): The description of the software development task to analyze.

### Output
Returns a `TaskAnalysis` object containing:
- **task** (`str`): The original task string.
- **complexity** (`str`): Estimated complexity (`low`, `medium`, `high`).
- **risk** (`str`): Estimated domain risk of the task (`low`, `medium`, `high`).
- **estimated_steps** (`int`): Estimated number of steps required to complete the task.
- **requires_review** (`bool`): Whether human review is recommended.
- **recommendation** (`str`): A textual recommendation based on the risk.

### Canonical Failures
- **`invalid_input`**: Returned natively by Agnara if the input does not match the inferred schema (e.g., passing an `int` instead of a `str` for `task`).

### Example Invocation Payload
```json
{
  "task": "Implement OAuth authentication, database migration and payment security"
}
```

### Example Result (Success)
```json
{
  "task": "Implement OAuth authentication, database migration and payment security",
  "complexity": "high",
  "risk": "high",
  "estimated_steps": 14,
  "requires_review": true,
  "recommendation": "Human review recommended before execution."
}
```
