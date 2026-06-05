from learn_unsloth_lab.ollama import plan_ollama
def test_ollama_plan(tmp_path): assert plan_ollama('configs/ollama.yaml',tmp_path)['commands'][0][:2]==['ollama','create']
