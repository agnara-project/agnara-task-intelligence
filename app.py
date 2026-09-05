from __future__ import annotations

import asyncio
from dataclasses import dataclass

from agnara import Agnara, Risk
from agnara.core.di import DIContainer, DIRegistry
from agnara.execution import (
    ExecutionContext,
    ExecutionPlan,
    Failure,
    Invocation,
    Success,
    invoke_result,
)


@dataclass
class TaskAnalysis:
    task: str
    complexity: str
    risk: str
    estimated_steps: int
    requires_review: bool
    recommendation: str


app = Agnara("task_intelligence")


@app.capability(
    description="Analyze a software development task.",
    scopes=("tasks:analyze",),
    risk=Risk.LOW,
    idempotent=True,
)
def analyze_task(task: str) -> TaskAnalysis:
    text = task.lower()

    keywords = (
        "oauth",
        "authentication",
        "database",
        "migration",
        "security",
        "payment",
        "architecture",
        "distributed",
        "production",
    )

    score = sum(1 for keyword in keywords if keyword in text)

    if score >= 3:
        complexity = "high"
        risk = "high"
    elif score >= 1:
        complexity = "medium"
        risk = "medium"
    else:
        complexity = "low"
        risk = "low"

    requires_review = risk == "high"

    return TaskAnalysis(
        task=task,
        complexity=complexity,
        risk=risk,
        estimated_steps=max(2, score * 2 + 2),
        requires_review=requires_review,
        recommendation=(
            "Human review recommended before execution."
            if requires_review
            else "Normal development workflow is sufficient."
        ),
    )


async def execute_task(
    task: str,
) -> None:
    capabilities = app.compile()

    definition = capabilities["task_intelligence.analyze_task"]

    dependencies = DIRegistry()

    plan = ExecutionPlan.compile(
        definition,
        dependencies,
    )

    outcome = await invoke_result(
        plan,
        ExecutionContext(
            Invocation(
                capability_id=definition.id,
                payload={
                    "task": task,
                },
                metadata={
                    "application": "agnara-task-intelligence",
                    "source": "cli",
                },
            ),
            DIContainer(dependencies),
        ),
    )

    print()
    print("AGNARA TASK INTELLIGENCE")
    print("=========================")

    print()
    print(f"Capability: {definition.id}")
    print(f"Description: {definition.description}")
    print(f"Risk: {definition.risk.value}")
    print(f"Scopes: {sorted(definition.scopes)}")

    print()
    print("Input schemas:")

    for name, schema in plan.input_schemas.items():
        print(f"  {name}: {schema}")

    print()
    print("RESULT")
    print("------")

    match outcome:
        case Success(value=value):
            print(f"Task: {value.task}")
            print(f"Complexity: {value.complexity}")
            print(f"Risk: {value.risk}")
            print(f"Estimated steps: {value.estimated_steps}")
            print(f"Requires review: {value.requires_review}")
            print(f"Recommendation: {value.recommendation}")

        case Failure(code=code, message=message):
            print(f"Failure code: {code}")
            print(f"Message: {message}")


async def main() -> None:
    task = input("Describe a software task: ")

    await execute_task(task)


if __name__ == "__main__":
    asyncio.run(main())
