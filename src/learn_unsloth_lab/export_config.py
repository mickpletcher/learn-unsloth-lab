from .config import load_yaml_config,require_keys
from .errors import ConfigError
SUPPORTED_QUANTIZATIONS={'f16','q8_0','q4_k_m','q5_k_m'}
def load_export_config(path):
 d=load_yaml_config(path); require_keys(d,['base_model','adapter_path','output_name','quantization'],'export config')
 if d['quantization'] not in SUPPORTED_QUANTIZATIONS: raise ConfigError(f"Unsupported quantization: {d['quantization']}")
 return d
