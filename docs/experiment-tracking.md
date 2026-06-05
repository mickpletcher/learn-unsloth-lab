# Experiment Tracking

Experiment tracking uses SQLite.

Default database:

```text
experiments\experiments.sqlite
```

## Initialize The Database

```powershell
.\scripts\init-experiments-db.ps1
```

Expected result:

```text
experiments/experiments.sqlite initialized
```

## Stored Fields

The database stores:

- Run ID.
- Model name.
- Dataset name.
- Config path.
- Config JSON.
- Metrics JSON.
- Status.
- Notes.
- Timestamps.
- Artifact paths.
- Export paths.

## CLI Commands

```powershell
python -m learn_unsloth_lab experiments list
python -m learn_unsloth_lab experiments show <run_id>
python -m learn_unsloth_lab reports
```

## Current Limits

Training dry runs write artifacts but do not automatically register every run in SQLite yet. The store is available for service use, reports, tests, and future CLI wiring.
