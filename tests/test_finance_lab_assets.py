from pathlib import Path
from learn_unsloth_lab.config import load_yaml_config
from learn_unsloth_lab.dataset_validation import validate_dataset
def test_finance_lab_assets():
 assert validate_dataset('datasets/finance-lab/train.jsonl')['valid']
 for p in ['configs/finance-lora.yaml','configs/finance-evaluation.yaml','configs/finance-export.yaml']:
  assert Path(p).exists() and load_yaml_config(p)
