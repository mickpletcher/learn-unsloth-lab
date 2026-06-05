from learn_unsloth_lab.dataset_validation import validate_dataset
def test_valid_sample_datasets():
 for p in ['datasets/alpaca-sample.json','datasets/chatml-sample.jsonl','datasets/sharegpt-sample.json','datasets/finance-instructions.jsonl']:
  assert validate_dataset(p)['valid']
