# Completed Upgrades

## 2026-06-05 v1 training lab buildout

Summary: Executed prompts 01 through 20 and built the offline safe Unsloth learning lab.

Changed files: `src/`, `configs/`, `datasets/`, `docs/`, `notebooks/`, `scripts/`, `tests/`, `.github/`, `README.md`, `CHANGELOG.md`, `assessment.md`, `future-upgrades.md`, `completed-upgrades.md`, `pyproject.toml`, and `requirements.txt`.

Validation: `python -m pytest`, `python -m ruff check .`, and `python -m learn_unsloth_lab --help`.

## 2026-06-05 documentation reconciliation

Summary: Refreshed the documentation set so the guides, folder README files, challenge files, assessment, and changelog match the current v1 CLI, configs, sample data, dry run behavior, generated artifacts, and known limits.

Changed files: `README.md`, `docs/`, `datasets/README.md`, `notebooks/README.md`, `CHANGELOG.md`, `assessment.md`, `future-upgrades.md`, and `completed-upgrades.md`.

Validation: `python -m pytest`, `python -m ruff check .`, `python -m learn_unsloth_lab --help`, and docs link validation.

## 2026-06-05 pytest asyncio warning cleanup

Summary: Set `asyncio_default_fixture_loop_scope` in `pyproject.toml` so pytest-asyncio no longer emits its fixture loop scope deprecation warning during test runs.

Changed files: `pyproject.toml`, `CHANGELOG.md`, `assessment.md`, and `completed-upgrades.md`.

Validation: `python -m pytest`, `python -m ruff check .`, and `python -m learn_unsloth_lab --help`.
