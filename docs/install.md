# Install

Use this guide from the repository root.

## What Gets Installed

The base install gives you the offline safe lab:

- CLI commands.
- Dataset validation and conversion.
- Dry run training.
- Evaluation reports.
- GGUF export planning.
- Ollama command planning.
- SQLite experiment tracking.
- Dashboard generation.
- Tests.

Real model training and real GGUF export need the optional ML dependencies, model access, and a CUDA GPU.

## Windows Install

```powershell
cd "C:\Users\mick0\OneDrive\Documents\Code & Dev\GitHub\learn-unsloth-lab"
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Expected result:

```text
Successfully installed learn-unsloth-lab
```

## Developer Tools

Install these before running tests or lint checks:

```powershell
python -m pip install -e .[dev]
```

## Optional ML Dependencies

Install these only on a machine prepared for local model work:

```powershell
python -m pip install -e .[ml]
```

The optional group includes Unsloth, Transformers, Datasets, PEFT, Torch, and Jupyter.

## Verify Install

```powershell
python -m learn_unsloth_lab --help
python -m pytest
python -m ruff check .
```

Expected result:

- CLI help prints command names.
- Tests pass.
- Ruff reports no issues.
