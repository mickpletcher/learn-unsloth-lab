# Datasets

This folder contains small synthetic datasets for validation, conversion, dry runs, and docs.

## Files

- `alpaca-sample.json`: Alpaca style records with `instruction`, optional `input`, and `output`.
- `chatml-sample.jsonl`: ChatML style records with `messages`.
- `sharegpt-sample.json`: ShareGPT style records with `conversations`.
- `finance-instructions.jsonl`: Normalized finance instruction examples.
- `finance-lab\train.jsonl`: Finance lab training examples.
- `finance-lab\eval-prompts.jsonl`: Finance lab evaluation prompts.

## Validate

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
```

## Convert

```powershell
python -m learn_unsloth_lab dataset convert datasets\alpaca-sample.json experiments\alpaca-normalized.jsonl
```

## Data Rules

- Keep examples synthetic.
- Do not add customer data.
- Do not add secrets.
- Keep files small enough for fast tests.
