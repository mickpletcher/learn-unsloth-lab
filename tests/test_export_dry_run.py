from learn_unsloth_lab.export import plan_gguf_export
def test_export_plan(tmp_path): assert plan_gguf_export('configs/export-gguf.yaml',output_root=tmp_path)['manifest'].endswith('export-manifest.json')
