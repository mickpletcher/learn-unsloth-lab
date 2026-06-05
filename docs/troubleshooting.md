# Troubleshooting

## PowerShell Path Has Spaces

Quote the path:

```powershell
cd "C:\Users\mick0\OneDrive\Documents\Code & Dev\GitHub\learn-unsloth-lab"
```

## Virtual Environment Is Not Active

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then verify:

```powershell
python -m learn_unsloth_lab --help
```

## Module Not Found

Reinstall editable mode:

```powershell
python -m pip install -e .
```

## Dataset Validation Fails

Run:

```powershell
python -m learn_unsloth_lab dataset validate <path>
```

Check for:

- Blank content.
- Missing assistant response.
- Invalid role.
- Invalid JSON.
- Wrong file path.

## Training Fails

Run dry run first:

```powershell
python -m learn_unsloth_lab train configs\finance-lora.yaml --dry-run
```

If dry run passes but real training fails, check:

- CUDA driver.
- PyTorch CUDA build.
- GPU memory.
- Model access.
- Optional ML dependency install.

## Ollama Fails

Use dry run first:

```powershell
python -m learn_unsloth_lab ollama create configs\ollama.yaml --dry-run
```

For real runs, confirm:

- Ollama is installed.
- `ollama` is on `PATH`.
- The GGUF file exists.

## Ruff Or Pytest Fails

Run:

```powershell
python -m pip install -e .[dev]
python -m pytest
python -m ruff check .
```

If failures persist, inspect the exact file and line in the output.
