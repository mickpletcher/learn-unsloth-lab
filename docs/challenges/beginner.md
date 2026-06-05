# Beginner Challenges

Goal: prove you can install the lab, validate data, and run CPU safe workflows.

## Challenge 1. Setup Check

```powershell
python -m learn_unsloth_lab --help
```

Completion criteria: command prints the CLI command list.

## Challenge 2. Dataset Validation

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
```

Completion criteria: output includes `"valid": true`.

## Challenge 3. Training Dry Run

```powershell
python -m learn_unsloth_lab train configs\example-training.yaml --dry-run
```

Expected artifact:

```text
experiments\example-training-dry-run\run.json
```

Completion criteria: run artifact exists.
