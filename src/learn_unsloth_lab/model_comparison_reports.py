from pathlib import Path


def write_model_comparison_report(plan, output_dir):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    markdown_path = output / "model-comparison.md"
    html_path = output / "model-comparison.html"
    rows = "".join(
        f"<tr><td>{row['family']}</td><td>{row['model']}</td><td>{row['dataset']}</td></tr>"
        for row in plan["runs"]
    )
    markdown_path.write_text("# Model Comparison\n", encoding="utf-8")
    html_path.write_text(
        "<html><body><h1>Model Comparison</h1><table>"
        + rows
        + "</table></body></html>",
        encoding="utf-8",
    )
    return {"markdown": str(markdown_path), "html": str(html_path)}
