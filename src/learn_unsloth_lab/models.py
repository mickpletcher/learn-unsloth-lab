from dataclasses import dataclass
from .errors import ModelError
@dataclass(frozen=True)
class ModelFamily: family:str; example_model:str; chat_template:str
MODEL_FAMILIES={'qwen':ModelFamily('qwen','unsloth/Qwen2.5-1.5B-Instruct','qwen'),'llama':ModelFamily('llama','unsloth/Llama-3.2-1B-Instruct','llama-3'),'gemma':ModelFamily('gemma','unsloth/gemma-2-2b-it','gemma'),'deepseek':ModelFamily('deepseek','unsloth/DeepSeek-R1-Distill-Qwen-1.5B','qwen')}
def get_model_family(name):
    try: return MODEL_FAMILIES[name.lower()]
    except KeyError as e: raise ModelError(f'Unsupported model family: {name}') from e
def unsloth_load_args(model_name,max_seq_length,load_in_4bit): return {'model_name':model_name,'max_seq_length':max_seq_length,'load_in_4bit':load_in_4bit}
def load_unsloth_model(**kw):
    try: from unsloth import FastLanguageModel
    except Exception as e: raise ModelError('Unsloth is not installed. Install ML extras in a GPU environment.') from e
    return FastLanguageModel.from_pretrained(**kw)
