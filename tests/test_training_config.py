from learn_unsloth_lab.training_config import load_training_config
def test_training_config_loads(): assert load_training_config('configs/qwen-lora.yaml')['training']['mode']=='lora'
