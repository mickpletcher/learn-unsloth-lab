from pathlib import Path
import json

from .experiment_store import list_experiments


def write_experiment_summary(db_path, output_dir):
    rows = list_experiments(db_path)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    json_path = output / "experiments-summary.json"
    markdown_path = output / "experiments-summary.md"
    json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    markdown_path.write_text(
        "# Experiments Summary\n\n"
        + "\n".join(f"- {row['run_id']}: {row['status']}" for row in rows)
        + "\n",
        encoding="utf-8",
    )
    return {"json": str(json_path), "markdown": str(markdown_path)}
