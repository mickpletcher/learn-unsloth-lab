# Training Guide

The training workflow is built around safe dry runs first.

Dry run mode validates the YAML config and writes artifacts. It does not load Unsloth, Torch, a model, or a dataset into GPU memory.

## Key Terms

LoRA means training small adapter weights instead of all base model weights.

QLoRA means using LoRA with quantized model loading to reduce GPU memory use.

An adapter is the small trained output that can later be merged or exported.

## Training Configs

Available configs:

- `configs\example-training.yaml`
- `configs\qwen-lora.yaml`
- `configs\llama-qlora.yaml`
- `configs\gemma-lora.yaml`
- `configs\deepseek-qlora.yaml`
- `configs\finance-lora.yaml`

Each config includes:

- Model family and base model name.
- Dataset path and format.
- LoRA or QLoRA mode.
- Rank, alpha, learning rate, epochs, batch size, and sequence length.
- Output directory.

## Run A Dry Run

```powershell
python -m learn_unsloth_lab train configs\finance-lora.yaml --dry-run
```

Expected artifacts:

```text
experiments\finance-lora-dry-run\resolved-config.yaml
experiments\finance-lora-dry-run\metrics.json
experiments\finance-lora-dry-run\run.json
experiments\finance-lora-dry-run\logs\training.log
```

## Real Training

Real training is intentionally not part of the default test suite.

Before real training, confirm:

- CUDA GPU is available.
- PyTorch CUDA build matches your driver.
- Optional ML dependencies are installed.
- The model can be downloaded or is available locally.
- The dataset validates successfully.

Install ML dependencies:

```powershell
python -m pip install -e .[ml]
```

Run without dry run only after the machine is ready:

```powershell
python -m learn_unsloth_lab train configs\finance-lora.yaml --no-dry-run
```

## Troubleshooting

If real training fails, first rerun the dry run. If dry run passes, the issue is likely CUDA, package compatibility, model access, or local memory.
