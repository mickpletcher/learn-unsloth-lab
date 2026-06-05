from pathlib import Path
import yaml
from .errors import ConfigError
def load_yaml_config(path):
    p=Path(path)
    if not p.exists(): raise ConfigError(f"Config file not found: {p}")
    try: data=yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    except yaml.YAMLError as e: raise ConfigError(f"Invalid YAML in {p}: {e}") from e
    if not isinstance(data,dict): raise ConfigError('Config root must be a mapping')
    return data
def require_keys(data,keys,context='config'):
    miss=[k for k in keys if k not in data]
    if miss: raise ConfigError(f"Missing required {context} keys: {', '.join(miss)}")
def write_yaml(path,data):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(yaml.safe_dump(data,sort_keys=False),encoding='utf-8'); return p
