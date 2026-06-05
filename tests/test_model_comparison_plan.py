from learn_unsloth_lab.model_comparison import plan_model_comparison
def test_model_comparison_plan(): assert {r['family'] for r in plan_model_comparison('configs/model-comparison.yaml')['runs']}=={'qwen','llama','gemma','deepseek'}
