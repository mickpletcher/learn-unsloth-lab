# Intermediate Challenges

Goal: use the CLI to convert data, evaluate prompts, and inspect reports.

## Challenge 1. Convert Dataset

```powershell
python -m learn_unsloth_lab dataset convert datasets\alpaca-sample.json experiments\alpaca-normalized.jsonl
```

Completion criteria: `experiments\alpaca-normalized.jsonl` exists and contains one JSON object per line.

## Challenge 2. Evaluation Report

```powershell
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-evaluation
```

Expected artifacts:

```text
experiments\finance-evaluation\evaluation-results.json
experiments\finance-evaluation\evaluation-report.html
```

Completion criteria: open the HTML report and identify adherence and similarity scores.

## Challenge 3. Experiment Report

```powershell
python -m learn_unsloth_lab reports
```

Completion criteria: summary report files are written under `experiments\reports`.
