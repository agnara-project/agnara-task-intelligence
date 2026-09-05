import pytest
from agnara import Risk
from agnara.core.di import DIContainer, DIRegistry
from agnara.execution import (
    ExecutionContext,
    ExecutionPlan,
    Failure,
    Invocation,
    Success,
    invoke_result,
)

from app import app


@pytest.fixture
def plan():
    capabilities = app.compile()
    definition = capabilities["task_intelligence.analyze_task"]
    dependencies = DIRegistry()
    return ExecutionPlan.compile(definition, dependencies)


@pytest.fixture
def container():
    return DIContainer(DIRegistry())


@pytest.mark.asyncio
async def test_analyze_task_low_risk(plan, container):
    outcome = await invoke_result(
        plan,
        ExecutionContext(
            Invocation(
                capability_id=plan.definition.id,
                payload={"task": "Create a contact page"},
                metadata={"source": "test"},
            ),
            container,
        ),
    )

    assert isinstance(outcome, Success)
    assert outcome.value.complexity == "low"
    assert outcome.value.risk == "low"
    assert outcome.value.requires_review is False
    assert outcome.value.estimated_steps == 2


@pytest.mark.asyncio
async def test_analyze_task_high_risk(plan, container):
    outcome = await invoke_result(
        plan,
        ExecutionContext(
            Invocation(
                capability_id=plan.definition.id,
                payload={
                    "task": "Implement OAuth authentication, database migration and payment security"
                },
                metadata={"source": "test"},
            ),
            container,
        ),
    )

    assert isinstance(outcome, Success)
    assert outcome.value.complexity == "high"
    assert outcome.value.risk == "high"
    assert outcome.value.requires_review is True
    # 'oauth', 'authentication', 'database', 'migration', 'payment', 'security' -> 6 keywords
    # score = 6, score * 2 + 2 = 14
    assert outcome.value.estimated_steps == 14


@pytest.mark.asyncio
async def test_analyze_task_invalid_input(plan, container):
    outcome = await invoke_result(
        plan,
        ExecutionContext(
            Invocation(
                capability_id=plan.definition.id,
                payload={"task": 12345},
                metadata={"source": "test"},
            ),
            container,
        ),
    )

    assert isinstance(outcome, Failure)
    assert outcome.code == "invalid_input"
    assert "expected str, got int" in outcome.message.lower()


def test_capability_metadata():
    capabilities = app.compile()
    definition = capabilities["task_intelligence.analyze_task"]

    assert str(definition.id) == "task_intelligence.analyze_task"
    assert definition.description == "Analyze a software development task."
    assert definition.scopes == frozenset({"tasks:analyze"})
    assert definition.risk == Risk.LOW
    assert definition.idempotency.value == "yes"


def test_schema_inference(plan):
    assert "task" in plan.input_schemas
