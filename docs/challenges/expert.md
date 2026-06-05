# Expert Challenges

Goal: interpret model comparison and release readiness.

## Challenge 1. Model Comparison Plan

```powershell
python -c "from learn_unsloth_lab.model_comparison import plan_model_comparison; print(plan_model_comparison('configs/model-comparison.yaml'))"
```

Completion criteria: output includes Qwen, Llama, Gemma, and DeepSeek.

## Challenge 2. Model Comparison Report

```powershell
python -c "from learn_unsloth_lab.model_comparison import plan_model_comparison; from learn_unsloth_lab.model_comparison_reports import write_model_comparison_report; plan=plan_model_comparison('configs/model-comparison.yaml'); print(write_model_comparison_report(plan, 'experiments/model-comparison'))"
```

Expected artifacts:

```text
experiments\model-comparison\model-comparison.md
experiments\model-comparison\model-comparison.html
```

## Challenge 3. Release Readiness Review

```powershell
python -m pytest
python -m ruff check .
python -m learn_unsloth_lab --help
```

Completion criteria: all commands pass and `assessment.md`, `CHANGELOG.md`, `future-upgrades.md`, and `completed-upgrades.md` reflect the current repo.
