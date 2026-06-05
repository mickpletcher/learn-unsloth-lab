# Evaluation Guide

Evaluation compares base model style output against fine tuned model style output for the same prompts.

The current implementation uses deterministic placeholder generators unless you call the Python API with custom generator functions. This keeps tests offline.

## Run Evaluation

```powershell
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-evaluation
```

Expected artifacts:

```text
experiments\finance-evaluation\evaluation-results.json
experiments\finance-evaluation\evaluation-report.html
```

## Metrics

The report includes:

- Base output.
- Fine tuned output.
- Base latency.
- Fine tuned latency.
- Base response length.
- Fine tuned response length.
- Prompt adherence score.
- Token overlap similarity score.
- Pass or fail result.

## Prompt File Format

Evaluation prompts use JSONL:

```json
{"prompt":"Summarize invoice INV-100","expected":"Concise educational finance response"}
```

## Current Limits

- Scoring is simple and rule based.
- It does not replace human review.
- Live model generation is not wired into the CLI yet.

Use the results as a learning report, not a production quality gate.
