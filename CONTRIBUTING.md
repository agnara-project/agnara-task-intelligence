# Contributing to Agnara Task Intelligence

Thank you for your interest in contributing! This project is Historical Reference Application #001 in the Agnara reference series, designed to showcase the framework as it existed in version `0.1.0a2`.

## Historical Context
Please understand that this project is intentionally constrained to demonstrate the early capabilities of Agnara. We will not accept PRs that introduce frameworks or architectures that bypass Agnara, or that depend on Agnara features released after `0.1.0a2`.

## Getting Started

1. **Fork & Branch**: Create a feature branch from `main`.
2. **Setup Environment**:
   Ensure you have Python 3.14+ installed.
   ```bash
   py -3.14 -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate # On Unix
   ```
3. **Install Dependencies**:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   pip install ruff pytest pytest-asyncio
   ```

## Development Rules
- **Maintain Python 3.14+ compatibility**.
- **Preserve Agnara `0.1.0a2` compatibility**.
- **No external frameworks** (like FastAPI, Flask, Pydantic) unless strictly necessary and justified.
- **Add Tests** for any behavior changes.
- **Update Documentation** if you change public interfaces or architecture.

## Quality Gates
Before submitting a PR, ensure the following pass:
```bash
ruff format --check .
ruff check .
python -m pytest tests/
python -c "import app"  # Smoke test
```

## Submitting a Pull Request
- Ensure your PR is small and focused.
- Provide a clear summary and motivation.
- Fill out the PR template completely.
- Ensure all CI checks pass.
