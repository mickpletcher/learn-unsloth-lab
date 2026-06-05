from learn_unsloth_lab.dashboard import generate_dashboard
def test_dashboard_render(tmp_path): assert generate_dashboard(output_dir=tmp_path)['html'].endswith('index.html')
