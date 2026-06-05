# Notebooks

The notebooks provide a guided learning path.

## Order

1. `01-first-fine-tune.ipynb`
2. `02-dataset-formatting.ipynb`
3. `03-qlora-training.ipynb`
4. `04-evaluation.ipynb`
5. `05-gguf-export.ipynb`

## Setup

```powershell
python -m pip install -e .[ml]
jupyter notebook
```

Use the base install if you only want to inspect notebooks and run CPU safe cells:

```powershell
python -m pip install -e .
```

## Notes

- GPU required sections are marked in notebook text.
- CPU safe cells use dry runs or sample files.
- Notebook existence is covered by `tests\test_notebooks_exist.py`.
