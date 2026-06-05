# Challenges

Use these tracks to prove you can run the lab end to end.

## Tracks

- `beginner.md`: Setup, dataset validation, and dry runs.
- `intermediate.md`: Evaluation, CLI use, and report review.
- `advanced.md`: GGUF export planning, Ollama planning, and sweeps.
- `expert.md`: Model comparison, interpretation, and release readiness.
- `completion-checklist.md`: One checklist for all artifacts.

## Baseline Validation

```powershell
python -m pytest
python -m ruff check .
```

## Expected Artifact Areas

- `experiments\`
- `exports\`

Generated artifacts are local outputs and should not be committed.
