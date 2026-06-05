from learn_unsloth_lab.export_config import load_export_config
def test_export_config(): assert load_export_config('configs/export-gguf.yaml')['quantization']=='q4_k_m'
