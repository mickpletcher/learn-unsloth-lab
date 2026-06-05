from pathlib import Path
import json
import subprocess

from .config import load_yaml_config
from .ollama_templates import DEFAULT_TEMPLATE


def generate_modelfile(config):
    lines = [f"FROM {config['gguf_path']}"]
    if config.get("system_prompt"):
        lines.append("SYSTEM " + json.dumps(config["system_prompt"]))
    lines.append("TEMPLATE " + json.dumps(config.get("template", DEFAULT_TEMPLATE)))
    for key, value in config.get("parameters", {}).items():
        lines.append(f"PARAMETER {key} {value}")
    return "\n".join(lines) + "\n"


def ollama_commands(config):
    return [
        ["ollama", "create", config["model_name"], "-f", "Modelfile"],
        *[["ollama", "run", config["model_name"], prompt] for prompt in config.get("test_prompts", [])],
    ]


def plan_ollama(config_path, output_dir="exports/ollama"):
    config = load_yaml_config(config_path)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    modelfile = output / "Modelfile"
    modelfile.write_text(generate_modelfile(config), encoding="utf-8")
    return {"modelfile": str(modelfile), "commands": ollama_commands(config)}


def run_ollama(config_path, dry_run=True):
    plan = plan_ollama(config_path)
    if dry_run:
        return plan | {"dry_run": True}
    outputs = []
    for command in plan["commands"]:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        outputs.append({"command": command, "stdout": result.stdout})
    output_path = Path(plan["modelfile"]).parent / "ollama-test-results.json"
    output_path.write_text(json.dumps(outputs, indent=2), encoding="utf-8")
    return plan | {"outputs": str(output_path), "dry_run": False}
