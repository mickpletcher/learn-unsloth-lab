import json
from pathlib import Path
def validate_export_manifest(path):
 m=json.loads(Path(path).read_text(encoding='utf-8')); req=['base_model','output_name','quantization','gguf_path','dry_run']; miss=[x for x in req if x not in m]; return {'valid':not miss,'missing':miss,'manifest':m}
