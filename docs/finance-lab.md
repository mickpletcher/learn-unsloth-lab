# Finance Lab

The finance lab is an educational example using synthetic records.

It covers:

- Budget categorization.
- Invoice summarization.
- Cash flow explanation.
- Policy Q&A.
- Risk wording.

It is not financial advice.

## Files

- `datasets\finance-lab\train.jsonl`
- `datasets\finance-lab\eval-prompts.jsonl`
- `configs\finance-lora.yaml`
- `configs\finance-evaluation.yaml`
- `configs\finance-export.yaml`

## Validate Training Data

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-lab\train.jsonl
```

## Training Dry Run

```powershell
python -m learn_unsloth_lab train configs\finance-lora.yaml --dry-run
```

## Evaluation

```powershell
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-lab\evaluation
```

## Export Plan

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
```

## Safety Notes

- Keep examples synthetic.
- Avoid personal financial data.
- Avoid claims of guaranteed returns.
- Treat generated output as educational only.
