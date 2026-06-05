# Quickstart

This path uses dry runs and sample data. It does not require a GPU.

## 1. Validate A Dataset

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
```

Expected result:

```json
{
  "valid": true
}
```

The full output also includes record count and validation details.

## 2. Convert Alpaca Data To JSONL

```powershell
python -m learn_unsloth_lab dataset convert datasets\alpaca-sample.json experiments\alpaca-normalized.jsonl
```

Expected artifact:

```text
experiments\alpaca-normalized.jsonl
```

## 3. Run A Training Dry Run

```powershell
python -m learn_unsloth_lab train configs\example-training.yaml --dry-run
```

Expected artifacts:

```text
experiments\example-training-dry-run\resolved-config.yaml
experiments\example-training-dry-run\metrics.json
experiments\example-training-dry-run\run.json
experiments\example-training-dry-run\logs\training.log
```

## 4. Generate An Evaluation Report

```powershell
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-evaluation
```

Expected artifacts:

```text
experiments\finance-evaluation\evaluation-results.json
experiments\finance-evaluation\evaluation-report.html
```

## 5. Plan GGUF Export

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
```

Expected artifact:

```text
exports\finance-lora\dry-run\export-manifest.json
```

## 6. Plan Ollama Import

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
```

Expected artifact:

```text
exports\ollama\Modelfile
```

## 7. Build Dashboard

```powershell
python -m learn_unsloth_lab dashboard
```

Open:

```text
experiments\dashboard\index.html
```
