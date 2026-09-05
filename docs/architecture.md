# Architecture

The architecture of this application demonstrates the decoupled execution model of Agnara.

## Concept: CLI != Agnara

The current CLI is simply the human entry point. It is not the core of the application. The business logic does not depend on the CLI, and it is executed through Agnara's independent runtime.

### Data Flow

```mermaid
flowchart TD
    USER(["User"]) --> CLI["CLI / app.py main"]
    CLI --> INV["Agnara Invocation"]
    INV --> CTX["Execution Context"]
    CTX --> PLAN["Compiled Execution Plan"]
    PLAN --> RUNTIME["Agnara Runtime"]
    RUNTIME --> CAP["task_intelligence.analyze_task"]
    CAP --> ANALYSIS["TaskAnalysis"]
    ANALYSIS --> RUNTIME
    RUNTIME --> RESULT["Canonical Result: Success / Failure"]
    RESULT --> CLI
    CLI --> USER
```

## Why This Matters

This architecture ensures that the business logic (the capability) does not conceptually depend on the transport layer. In this reference application, we use a CLI to trigger the execution, but the capability itself is completely agnostic to whether it was invoked via CLI, HTTP, MCP, or another protocol.

Agnara handles the inference of schemas, input validation, and the structured return of `Success` or `Failure`.
