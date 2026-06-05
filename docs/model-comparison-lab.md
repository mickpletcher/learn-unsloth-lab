# Model Comparison Lab

The model comparison lab plans a consistent comparison across:

- Qwen.
- Llama.
- Gemma.
- DeepSeek.

## Config

Use:

```text
configs\model-comparison.yaml
```

## Current Access Pattern

There is no CLI command for model comparison yet. Use the Python API:

```powershell
python -c "from learn_unsloth_lab.model_comparison import plan_model_comparison; print(plan_model_comparison('configs/model-comparison.yaml'))"
```

## Report Generation

```powershell
python -c "from learn_unsloth_lab.model_comparison import plan_model_comparison; from learn_unsloth_lab.model_comparison_reports import write_model_comparison_report; plan=plan_model_comparison('configs/model-comparison.yaml'); print(write_model_comparison_report(plan, 'experiments/model-comparison'))"
```

Expected artifacts:

```text
experiments\model-comparison\model-comparison.md
experiments\model-comparison\model-comparison.html
```

## Current Limits

Reports are based on planned runs and available experiment records. They do not train all four models automatically.
