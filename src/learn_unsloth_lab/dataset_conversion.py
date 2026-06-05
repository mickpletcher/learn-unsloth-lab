from pathlib import Path
import json

from .dataset_formats import normalize_record
from .dataset_validation import read_records, validate_messages
from .errors import DatasetError


def clean_normalized(rows):
    output = []
    seen = set()
    for row in rows:
        messages = [
            item for item in row["messages"] if str(item.get("content", "")).strip()
        ]
        key = json.dumps({"messages": messages}, sort_keys=True)
        if key in seen or validate_messages(messages):
            continue
        seen.add(key)
        output.append({"messages": messages})
    return output


def convert_to_jsonl(input_path, output_path):
    rows = read_records(input_path)
    output_rows = clean_normalized([normalize_record(row) for row in rows])
    if not output_rows:
        raise DatasetError("No valid records after cleaning")
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row) for row in output_rows) + "\n",
        encoding="utf-8",
    )
    return {
        "input_records": len(rows),
        "output_records": len(output_rows),
        "output_path": str(path),
    }
