from pathlib import Path
import json,html
def write_evaluation_reports(results,outdir):
 o=Path(outdir); o.mkdir(parents=True,exist_ok=True); jp=o/'evaluation-results.json'; hp=o/'evaluation-report.html'; jp.write_text(json.dumps({'results':results},indent=2),encoding='utf-8')
 rows=''.join('<tr>'+''.join(f"<td>{html.escape(str(r.get(c,'')))}</td>" for c in ['prompt','base_output','fine_tuned_output','similarity','adherence','passed'])+'</tr>' for r in results)
 hp.write_text('<html><body><h1>Evaluation Report</h1><table>'+rows+'</table></body></html>',encoding='utf-8'); return {'json':str(jp),'html':str(hp)}
