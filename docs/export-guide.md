# Export Guide

The export workflow plans GGUF output from a base model and adapter.

GGUF is a local model file format used by llama.cpp and local runtimes such as Ollama.

## Supported Quantization Values

- `f16`
- `q8_0`
- `q4_k_m`
- `q5_k_m`

Quantization reduces model size. Smaller files are easier to run locally but can reduce quality.

## Plan Export

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
```

Expected artifact:

```text
exports\finance-lora\dry-run\export-manifest.json
```

The manifest includes:

- Base model.
- Adapter path.
- Output name.
- Quantization.
- Planned GGUF path.
- Dry run status.

## Real Export

Real export requires:

- A trained adapter.
- Base model access.
- Unsloth installed.
- Enough disk space.
- A machine prepared for local model work.

Run real export only after those are ready:

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --no-dry-run
```

## Current Limits

Dry run export creates a manifest. It does not create a `.gguf` model file.
