# Ollama Guide

The Ollama workflow creates a Modelfile and command plan for local inference.

Ollama is a local runtime for running model packages. This repo does not require Ollama for tests.

## Plan Ollama Import

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
```

Expected artifact:

```text
exports\ollama\Modelfile
```

The command output also includes planned commands such as:

```text
ollama create finance-qwen-lora -f Modelfile
ollama run finance-qwen-lora "Summarize this invoice"
```

## Config Fields

`configs\ollama.yaml` includes:

- Model name.
- GGUF path.
- System prompt.
- Parameters.
- Test prompts.

## Real Ollama Run

Install Ollama first, then run:

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --no-dry-run
```

Real mode expects Ollama to be on `PATH` and the GGUF path to exist.

## Current Limits

Dry run mode writes a Modelfile and prints commands. It does not import or run a model.
