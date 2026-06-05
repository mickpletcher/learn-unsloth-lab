from learn_unsloth_lab.evaluation import run_evaluation
def test_evaluation_report(tmp_path): assert run_evaluation('datasets/finance-lab/eval-prompts.jsonl',tmp_path)['reports']['html'].endswith('evaluation-report.html')
