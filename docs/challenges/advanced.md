# Advanced Challenges

Goal: plan local model packaging and controlled experiments.

## Challenge 1. GGUF Export Plan

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
```

Expected artifact:

```text
exports\finance-lora\dry-run\export-manifest.json
```

Completion criteria: manifest includes output name and quantization.

## Challenge 2. Ollama Plan

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
```

Expected artifact:

```text
exports\ollama\Modelfile
```

Completion criteria: Modelfile includes `FROM`, `SYSTEM`, `TEMPLATE`, and `PARAMETER` lines.

## Challenge 3. Hyperparameter Sweep Plan

```powershell
python -c "from learn_unsloth_lab.hyperparameters import plan_sweep; print(plan_sweep('configs/hyperparameter-sweep.yaml'))"
```

Completion criteria: eight planned runs are generated.
