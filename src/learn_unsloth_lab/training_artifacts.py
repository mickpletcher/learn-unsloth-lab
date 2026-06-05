from pathlib import Path
from datetime import datetime, timezone
import json

from .config import write_yaml


def create_run_dir(base_dir="experiments", run_id=None):
    resolved_id = run_id or datetime.now(timezone.utc).strftime("run-%Y%m%d%H%M%S")
    run_dir = Path(base_dir) / resolved_id
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    (run_dir / "adapters").mkdir(exist_ok=True)
    return run_dir


def write_training_artifacts(run_dir, config, metrics, run):
    paths = {
        "resolved_config": write_yaml(run_dir / "resolved-config.yaml", config),
        "metrics": run_dir / "metrics.json",
        "run": run_dir / "run.json",
        "log": run_dir / "logs" / "training.log",
    }
    paths["metrics"].write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    paths["run"].write_text(json.dumps(run, indent=2), encoding="utf-8")
    paths["log"].write_text("dry run completed\n", encoding="utf-8")
    return {key: str(value) for key, value in paths.items()}
