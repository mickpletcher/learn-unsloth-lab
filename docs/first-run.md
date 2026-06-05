# First Run

This checklist starts from a fresh clone and ends with a working dry run.

## 1. Install

```powershell
cd "C:\Users\mick0\OneDrive\Documents\Code & Dev\GitHub\learn-unsloth-lab"
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
```

## 2. Verify Package And Tests

```powershell
python -m learn_unsloth_lab --help
python -m pytest
python -m ruff check .
```

Expected result:

- CLI help prints.
- Tests pass.
- Ruff passes.

## 3. Validate Sample Data

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
```

Expected result:

```text
"valid": true
```

## 4. Run Training Dry Run

```powershell
python -m learn_unsloth_lab train configs\example-training.yaml --dry-run
```

Expected artifacts:

```text
experiments\example-training-dry-run\run.json
experiments\example-training-dry-run\metrics.json
```

## 5. Generate Dashboard

```powershell
python -m learn_unsloth_lab dashboard
```

Open:

```text
experiments\dashboard\index.html
```
