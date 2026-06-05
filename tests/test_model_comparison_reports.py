from learn_unsloth_lab.model_comparison import plan_model_comparison
from learn_unsloth_lab.model_comparison_reports import write_model_comparison_report
def test_model_report(tmp_path): assert write_model_comparison_report(plan_model_comparison('configs/model-comparison.yaml'),tmp_path)['html'].endswith('model-comparison.html')
