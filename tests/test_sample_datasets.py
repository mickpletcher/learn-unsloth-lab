from learn_unsloth_lab.dataset_validation import read_records,validate_dataset
def test_sample_datasets_have_ten_records():
 for p in ['datasets/alpaca-sample.json','datasets/chatml-sample.jsonl','datasets/sharegpt-sample.json','datasets/finance-instructions.jsonl']:
  assert len(read_records(p))>=10 and validate_dataset(p)['valid']
