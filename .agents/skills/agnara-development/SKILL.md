---
name: agnara-development
description: Guidelines for developing with Agnara in this historical reference application.
---

# Agnara Development Guidelines

This project is a **historical reference application** built to demonstrate `agnara==0.1.0a2`.
It must remain compatible with this specific version.

## Core Principles
- **No External Frameworks**: Do not introduce HTTP servers (FastAPI, Flask), ORMs, or Pydantic unless strictly required for a non-Agnara purpose. This app must demonstrate **Agnara using Agnara**.
- **Historical Accuracy**: Do not use APIs that were added to Agnara after version `0.1.0a2`.
- **Validation**: Agnara handles input validation via its schemas. Let Agnara reject invalid types and return canonical `Failure(code="invalid_input", ...)` results. Do not write custom manual type checking for capabilities inputs if Agnara does it.

## Key Concepts to Demonstrate
- Capability registration using `@app.capability(...)`.
- Explicit `scopes`, `risk`, and `idempotent` metadata.
- Compiling an `ExecutionPlan`.
- Constructing an `ExecutionContext` and `Invocation`.
- Using `invoke_result` to get `Success` or `Failure`.

## How to Check Compatibility
Always run tests and smoke tests to ensure your changes work with the pinned Agnara version.
