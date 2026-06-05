# v1 Release Notes

Version 1.0.0 includes:

- Offline safe dataset validation and conversion.
- Dry run LoRA and QLoRA training planning.
- Evaluation metrics and JSON plus HTML reports.
- GGUF export planning.
- Ollama Modelfile and command planning.
- SQLite experiment tracking services and reports.
- Model comparison planning.
- Hyperparameter sweep planning.
- Synthetic sample datasets and a finance lab.
- Five learning notebooks.
- Typer CLI commands for the main workflows.
- Pytest and Ruff validation.
- GitHub Actions for CI and dependency scanning.
- Windows first documentation.
- Guided challenges.
- Static local dashboard.

Known limits:

- Real training needs CUDA GPU support and optional ML dependencies.
- Real export needs model artifacts and Unsloth.
- Hyperparameter sweeps and model comparison use Python service functions, not dedicated CLI commands yet.
- Evaluation scoring is simple and rule based.
