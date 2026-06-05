# learn-unsloth-lab

[![CI](https://github.com/mick/learn-unsloth-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/mick/learn-unsloth-lab/actions/workflows/ci.yml)
[![Security](https://github.com/mick/learn-unsloth-lab/actions/workflows/security.yml/badge.svg)](https://github.com/mick/learn-unsloth-lab/actions/workflows/security.yml)

This repository is a hands on lab for learning practical fine tuning workflows with Unsloth.

You can use it to learn:
- Dataset validation and conversion
- LoRA and QLoRA training flow
- Evaluation and experiment tracking
- GGUF export planning
- Ollama packaging planning
- Local HTML dashboard reporting

## Quick Links

- Changelog: [CHANGELOG.md](CHANGELOG.md)
- Completed upgrades: [completed-upgrades.md](completed-upgrades.md)
- Future upgrades: [future-upgrades.md](future-upgrades.md)
- Windows setup: [docs/windows-setup.md](docs/windows-setup.md)
- First run checklist: [docs/first-run.md](docs/first-run.md)
- CLI reference: [docs/cli-reference.md](docs/cli-reference.md)
- Troubleshooting: [docs/troubleshooting.md](docs/troubleshooting.md)

## Who This Is For

This lab is built for beginners and intermediate users.

If you are new, start with dry run commands first. Dry runs validate your setup and config without loading models.

## What Key Terms Mean

- LoRA: Fine tuning by training small adapter layers instead of all model weights.
- QLoRA: LoRA workflow with quantized model loading, commonly 4 bit.
- GGUF: Local model file format used by many local inference tools.
- Ollama: Local runtime for running model packages on your machine.

## Requirements

Minimum requirements:
- PowerShell or Bash shell
- Python 3.11+
- Internet access for package install

Optional for full training:
- NVIDIA CUDA GPU
- ML extras from this project

## Installation On Windows

From repo root, run:

```powershell
cd "C:\Users\mick0\OneDrive\Documents\Code & Dev\GitHub\learn-unsloth-lab"
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Optional ML dependencies for real model training:

```powershell
python -m pip install -e .[ml]
```

Developer and test tools:

```powershell
python -m pip install -e .[dev]
```

## Installation On Linux

From repo root, run:

```bash
cd /path/to/learn-unsloth-lab
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Optional ML dependencies for real model training:

```bash
python -m pip install -e .[ml]
```

Developer and test tools:

```bash
python -m pip install -e .[dev]
```

## Installation On macOS

From repo root, run:

```bash
cd /path/to/learn-unsloth-lab
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Optional ML dependencies for real model training:

```bash
python -m pip install -e .[ml]
```

Developer and test tools:

```bash
python -m pip install -e .[dev]
```

## Verify Your Setup

Run these checks:

```powershell
python -m pytest
python -m ruff check .
python -m learn_unsloth_lab --help
```

Expected result:
- Tests pass
- Ruff reports no lint errors
- CLI help prints command list

## Fast Start For New Users

Copy and run this sequence in order:

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
python -m learn_unsloth_lab dataset convert datasets\alpaca-sample.json experiments\alpaca-normalized.jsonl
python -m learn_unsloth_lab train configs\example-training.yaml --dry-run
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-evaluation
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
python -m learn_unsloth_lab reports
python -m learn_unsloth_lab dashboard
```

Then open:
- `experiments/dashboard/index.html`

## Full Workflow Guide

### 1. Validate Your Dataset

Use this before every training run.

```powershell
python -m learn_unsloth_lab dataset validate datasets\finance-instructions.jsonl
```

This command checks structure and returns JSON output with validity details.

### 2. Convert Datasets To Normalized JSONL

Supported input styles include Alpaca, ChatML, and ShareGPT.

```powershell
python -m learn_unsloth_lab dataset convert datasets\sharegpt-sample.json experiments\sharegpt-normalized.jsonl
```

Output is normalized chat style JSONL with `messages`.

### 3. Run Training Dry Run First

Dry run is the safest first step and works offline.

```powershell
python -m learn_unsloth_lab train configs\finance-lora.yaml --dry-run
```

Dry run validates config and writes planning artifacts without model loading.

### 4. Run Evaluation

Evaluation compares responses and reports metrics such as latency, length, adherence, and similarity.

```powershell
python -m learn_unsloth_lab evaluate datasets\finance-lab\eval-prompts.jsonl --output experiments\finance-evaluation
```

### 5. Plan GGUF Export

Use dry run first.

```powershell
python -m learn_unsloth_lab export gguf configs\finance-export.yaml --dry-run
```

Supported quantization planning modes include `f16`, `q8_0`, `q4_k_m`, and `q5_k_m`.

### 6. Plan Ollama Package

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
```

This creates a Modelfile plan and command guidance.

### 7. Track Experiments

List experiment runs:

```powershell
python -m learn_unsloth_lab experiments list
```

Show one run:

```powershell
python -m learn_unsloth_lab experiments show <run_id>
```

Generate summary reports:

```powershell
python -m learn_unsloth_lab reports
```

### 8. Build Dashboard

```powershell
python -m learn_unsloth_lab dashboard
```

Open `experiments/dashboard/index.html` in your browser.

## CLI Commands At A Glance

- `dataset validate`
- `dataset convert`
- `train`
- `evaluate`
- `export gguf`
- `ollama create`
- `experiments list`
- `experiments show`
- `reports`
- `dashboard`

## Repository Layout

- `src/learn_unsloth_lab`: CLI and core implementation
- `configs`: Ready to use YAML configs
- `datasets`: Sample datasets and finance lab prompts
- `docs`: Topic guides for setup, training, export, evaluation, and more
- `notebooks`: Guided learning notebooks
- `experiments`: Local generated outputs and reports
- `exports`: Local generated export artifacts
- `tests`: Offline test coverage
- `scripts`: Utility scripts

## Learning Path For Beginners

Suggested order:
1. [docs/windows-setup.md](docs/windows-setup.md)
2. [docs/first-run.md](docs/first-run.md)
3. [docs/dataset-guide.md](docs/dataset-guide.md)
4. [docs/training-guide.md](docs/training-guide.md)
5. [docs/evaluation-guide.md](docs/evaluation-guide.md)
6. [docs/export-guide.md](docs/export-guide.md)
7. [docs/ollama-guide.md](docs/ollama-guide.md)
8. [docs/dashboard.md](docs/dashboard.md)
9. [docs/testing.md](docs/testing.md)

Hands on practice:
1. [docs/challenges/README.md](docs/challenges/README.md)
2. [notebooks/README.md](notebooks/README.md)

## Troubleshooting Basics

If a command fails:
1. Confirm virtual environment is active.
2. Run `python -m learn_unsloth_lab --help`.
3. Re run `python -m pip install -e .`.
4. Validate config path and dataset path.
5. Review [docs/troubleshooting.md](docs/troubleshooting.md).

## Notes On Outputs

- This project keeps generated artifacts in `experiments` and `exports`.
- Repository defaults are designed for offline safe learning workflows.
- Dry run commands are recommended before any real training or export.

## License

MIT. See [LICENSE](LICENSE).
