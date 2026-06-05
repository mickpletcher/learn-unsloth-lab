from .config import load_yaml_config
from .models import MODEL_FAMILIES
def plan_model_comparison(path):
 c=load_yaml_config(path); ds=c.get('dataset','datasets/finance-instructions.jsonl'); return {'objective':c.get('objective','comparison'),'runs':[{'family':k,'model':v.example_model,'dataset':ds} for k,v in MODEL_FAMILIES.items()]}
