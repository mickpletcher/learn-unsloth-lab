from .config import load_yaml_config,require_keys
from .errors import ConfigError
from .models import MODEL_FAMILIES
def load_training_config(path):
 d=load_yaml_config(path); require_keys(d,['model','dataset','training','output'],'training config'); require_keys(d['model'],['family','name'],'model')
 if d['model']['family'] not in MODEL_FAMILIES: raise ConfigError(f"Unsupported model family: {d['model']['family']}")
 if d['training'].get('mode','lora') not in {'lora','qlora'}: raise ConfigError('training.mode must be lora or qlora')
 return d
