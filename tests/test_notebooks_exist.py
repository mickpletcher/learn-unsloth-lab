import json
from pathlib import Path
def test_notebooks_have_markdown_and_code():
 for p in Path('notebooks').glob('*.ipynb'):
  data=json.loads(p.read_text(encoding='utf-8')); types={c['cell_type'] for c in data['cells']}; assert {'markdown','code'} <= types
