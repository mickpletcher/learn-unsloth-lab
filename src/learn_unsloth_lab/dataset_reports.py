from pathlib import Path
import json

from .dataset_formats import normalize_record
from .dataset_validation import read_records, validate_records


def dataset_stats(path):
    rows = read_records(path)
    normalized = [normalize_record(row) for row in rows]
    roles = {}
    prompts = []
    responses = []
    for row in normalized:
        for message in row["messages"]:
            roles[message["role"]] = roles.get(message["role"], 0) + 1
            word_count = len(message["content"].split())
            if message["role"] == "assistant":
                responses.append(word_count)
            else:
                prompts.append(word_count)
    return {
        "record_count": len(rows),
        "role_counts": roles,
        "avg_prompt_words": round(sum(prompts) / max(len(prompts), 1), 2),
        "avg_response_words": round(sum(responses) / max(len(responses), 1), 2),
        "estimated_tokens": int((sum(prompts) + sum(responses)) * 1.3),
        "validation": validate_records(rows),
    }


def write_dataset_report(path, output_dir):
    stats = dataset_stats(path)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    json_path = output / "dataset-report.json"
    markdown_path = output / "dataset-report.md"
    json_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    markdown_path.write_text(
        f"# Dataset Report\n\nRecords: {stats['record_count']}\n\n"
        f"Estimated tokens: {stats['estimated_tokens']}\n",
        encoding="utf-8",
    )
    return {"json": str(json_path), "markdown": str(markdown_path)}
