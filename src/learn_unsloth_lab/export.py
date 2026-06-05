from pathlib import Path
from importlib.util import find_spec
import json
from .export_config import load_export_config
def plan_gguf_export(config_path,run_id='dry-run',output_root='exports'):
 c=load_export_config(config_path); o=Path(output_root)/c['output_name']/run_id; o.mkdir(parents=True,exist_ok=True); gg=o/f"{c['output_name']}-{c['quantization']}.gguf"; m=c|{'gguf_path':str(gg),'dry_run':True}; mp=o/'export-manifest.json'; mp.write_text(json.dumps(m,indent=2),encoding='utf-8'); return {'status':'planned','manifest':str(mp),'gguf_path':str(gg)}
def export_gguf(config_path,dry_run=True):
 if dry_run: return plan_gguf_export(config_path)
 if find_spec("unsloth") is None:
  from .errors import ExportError
  raise ExportError('Real GGUF export requires Unsloth and model artifacts')
 return plan_gguf_export(config_path)|{'status':'completed'}
