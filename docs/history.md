# Historical Baseline

This document preserves the context of this project's creation.

**Agnara Task Intelligence** is the first historical reference application built externally with Agnara from its public PyPI distribution. It serves to demonstrate the framework's core concepts as they existed early in its lifecycle.

## Environment & Dependencies
- **Framework:** Agnara
- **Agnara Version:** `0.1.0a2`
- **Python Baseline:** `>=3.14`
- **Initial Validated Interpreter:** `CPython 3.14.4`
- **Distribution Source:** PyPI

## Application Details
- **Primary Interface:** CLI
- **Primary Capability:** `task_intelligence.analyze_task`

## What This Project Demonstrates
This project demonstrates the kernel of Agnara available at the time of version `0.1.0a2`:
- Capability registration via decorators
- Capability metadata (`scopes`, `risk`, `idempotent`)
- Schema inference from Python type hints
- Execution plan compilation
- Canonical invocation and execution context
- Canonical success and failure responses (`Success`, `Failure`)
- Input validation (rejecting invalid types natively)
- Completely independent execution, decoupled from HTTP, FastAPI, Flask, Django, MCP, or other transports

## What This Project Does NOT Demonstrate
Because this project is pinned to `0.1.0a2`, it explicitly does **not** demonstrate:
- Transports like HTTP, MCP, or A2A
- Advanced event systems
- Features added to Agnara in subsequent releases

## Future Evolution
When Agnara evolves, we will NOT rewrite the history of this repository to include those newer features. This repository will remain a snapshot of how applications were built with Agnara in its early days. Future capabilities of Agnara will be demonstrated in separate, newer reference applications.
