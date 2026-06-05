# Dataset Guide

The dataset tools validate, clean, summarize, and convert small instruction datasets.

## Supported Formats

Alpaca:

```json
{
  "instruction": "Explain budget variance.",
  "input": "",
  "output": "Budget variance is the difference between planned and actual spend."
}
```

ChatML:

```json
{
  "messages": [
    {"role": "user", "content": "Summarize this invoice."},
    {"role": "assistant", "content": "Extract vendor, due date, and amount due."}
  ]
}
```

ShareGPT:

```json
{
  "conversations": [
    {"from": "human", "value": "Categorize this receipt."},
    {"from": "gpt", "value": "Classify the receipt by spend category."}
  ]
}
```

## Validate Data

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
```

Validation checks:

- File exists.
- JSON or JSONL can be parsed.
- Records can be normalized.
- Messages use valid roles.
- Each record includes an assistant reply.
- Message content is not blank.

## Convert Data

```powershell
python -m learn_unsloth_lab dataset convert datasets\sharegpt-sample.json experiments\sharegpt-normalized.jsonl
```

The output is normalized JSONL:

```json
{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
```

## Sample Files

- `datasets\alpaca-sample.json`
- `datasets\chatml-sample.jsonl`
- `datasets\sharegpt-sample.json`
- `datasets\finance-instructions.jsonl`
- `datasets\finance-lab\train.jsonl`
- `datasets\finance-lab\eval-prompts.jsonl`

## Safety Rules

- Use synthetic data for examples.
- Do not add customer data.
- Do not add passwords, tokens, access keys, or private financial details.
