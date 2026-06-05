from pathlib import Path
import html


def write_sweep_report(plan, output_dir):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    markdown_path = output / "sweep-report.md"
    html_path = output / "sweep-report.html"
    markdown_path.write_text(
        f"# Sweep Report\n\nRuns: {plan['run_count']}\n",
        encoding="utf-8",
    )
    html_path.write_text(
        "<html><body><h1>Sweep Report</h1>"
        + "".join(
            f"<p>{row['run']}: {html.escape(str(row['parameters']))}</p>"
            for row in plan["runs"]
        )
        + "</body></html>",
        encoding="utf-8",
    )
    return {"markdown": str(markdown_path), "html": str(html_path)}
