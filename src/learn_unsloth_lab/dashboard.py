from pathlib import Path
from .dashboard_data import collect_dashboard_data,write_dashboard_data
from .dashboard_templates import render_dashboard
def generate_dashboard(root='.',output_dir='experiments/dashboard'):
 data=collect_dashboard_data(root); o=Path(output_dir); o.mkdir(parents=True,exist_ok=True); dp=write_dashboard_data(data,o); hp=o/'index.html'; hp.write_text(render_dashboard(data),encoding='utf-8'); return {'html':str(hp),'data':str(dp)}
