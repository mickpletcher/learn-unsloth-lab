from pathlib import Path
import json
def collect_dashboard_data(root='.'):
 b=Path(root); g=lambda p: sorted(str(x.relative_to(b)) for x in p.glob('**/*') if x.is_file()) if p.exists() else []
 return {'datasets':g(b/'datasets'),'exports':g(b/'exports'),'reports':g(b/'experiments'),'challenges':g(b/'docs'/'challenges')}
def write_dashboard_data(data,outdir):
 o=Path(outdir); o.mkdir(parents=True,exist_ok=True); p=o/'dashboard-data.json'; p.write_text(json.dumps(data,indent=2),encoding='utf-8'); return p
