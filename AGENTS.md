# Agent Guidelines

## Mission
This repository is Historical Reference Application #001 in the Agnara reference series. It must remain a clean, professional, and reproducible demonstration of Agnara's early capabilities.

## Historical Constraint
Agents must preserve the historical context of this project. Do not upgrade Agnara to use features that were not present in `0.1.0a2`. Do not introduce large, external frameworks (like FastAPI) unless explicitly required for a non-framework capability. 

## Source of Truth
When making decisions, rely on the following hierarchy of authority:
1. Current task / issue
2. AGENTS.md
3. Architecture documentation (`docs/architecture.md`)
4. Tests
5. Project documentation
6. Implementation

## Before Working
1. Check `git status`.
2. Read `README.md`, `AGENTS.md`, `ARCHITECTURE.md` (or `docs/architecture.md`), and `CONTRIBUTING.md`.

## Scope Discipline
- Do NOT add unrequested features.
- Do NOT introduce frameworks to replace what Agnara already demonstrates.

## Agnara Compatibility
- Do not upgrade the Agnara dependency or migrate this repository to newer Agnara APIs as part of ordinary maintenance.
- This repository intentionally preserves the `agnara==0.1.0a2` historical baseline. A baseline migration requires an explicit historical-maintenance decision.
- Do not use features from the `main` branch of the Agnara repository if they do not exist in the pinned version.

## Testing & Quality Gates
Before finishing your work, you MUST ensure:
- Format and Lint pass (`ruff format --check .` and `ruff check .`)
- Tests pass (`python -m pytest tests/`)
- Smoke tests pass
- `git diff` and `git status` are reviewed.

## Attribution
Respect co-author policies. Do not invent agent identities or emails.

## Documentation
Any significant change must be reflected in `docs/` and `CHANGELOG.md`.

## Security
- NO SECRETS.
- NO CREDENTIALS.
- NO REAL TOKENS.

## Git Operations
- No force push.
- No deleting tags.
- No rewriting shared history.
- Do not commit or push unless explicitly authorized by the task.

## Agent Compatibility
This repository is designed to be compatible with multiple AI coding agents (Codex, Claude Code, Gemini/Antigravity, etc.). The rules in this file are the central contract. Do not create divergent rules for different agents.
