import pytest
from learn_unsloth_lab.config import load_yaml_config
from learn_unsloth_lab.errors import ConfigError
def test_load_yaml_config(): assert load_yaml_config('configs/example-training.yaml')['model']['family']=='qwen'
def test_missing_config_raises(tmp_path):
 with pytest.raises(ConfigError): load_yaml_config(tmp_path/'missing.yaml')
