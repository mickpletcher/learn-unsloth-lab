# CLI Reference

Run all commands from the repository root after activating your virtual environment.

## Help

```powershell
python -m learn_unsloth_lab --help
```

Commands:

- `dataset`
- `train`
- `evaluate`
- `export`
- `ollama`
- `experiments`
- `reports`
- `dashboard`

## Dataset Commands

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
python -m learn_unsloth_lab dataset convert datasets\alpaca-sample.json experiments\alpaca-normalized.jsonl
```

## Training Command

```powershell
python -m learn_unsloth_lab train configs\finance-lora.yaml --dry-run
```

Use `--no-dry-run` only on a GPU ready machine with optional ML dependencies installed.

## Evaluation Command

```powershell
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-evaluation
```

## Export Command

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
```

## Ollama Command

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
```

## Experiment Commands

```powershell
python -m learn_unsloth_lab experiments list
python -m learn_unsloth_lab experiments show <run_id>
```

## Reports Command

```powershell
python -m learn_unsloth_lab reports
```

## Dashboard Command

```powershell
python -m learn_unsloth_lab dashboard
```

## Exit Behavior

Dataset validation returns a nonzero exit code when validation fails. Other commands raise errors for missing configs, unsupported values, or missing external tools in real mode.
