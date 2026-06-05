# Testing

The test suite is offline by default.

It does not require:

- GPU.
- Network.
- Ollama.
- Model downloads.
- Real training.

## Run Tests

```powershell
python -m pytest
```

Expected result:

```text
28 passed
```

The exact runtime can vary.

## Run Ruff

```powershell
python -m ruff check .
```

Expected result:

```text
All checks passed!
```

## CLI Smoke Test

```powershell
python -m learn_unsloth_lab --help
```

Expected result:

```text
Commands
dataset
train
evaluate
export
ollama
experiments
reports
dashboard
```

## Test Coverage Areas

- Config loading.
- Dataset validation.
- Dataset conversion.
- Training dry runs.
- Evaluation metrics and reports.
- GGUF export planning.
- Ollama Modelfile planning.
- Hyperparameter sweep planning.
- SQLite experiment store.
- Model comparison planning.
- Notebook existence.
- Dashboard rendering.
- CLI commands.
