from learn_unsloth_lab.dataset_reports import write_dataset_report
def test_dataset_report(tmp_path): assert write_dataset_report('datasets/finance-instructions.jsonl',tmp_path)['markdown'].endswith('dataset-report.md')
