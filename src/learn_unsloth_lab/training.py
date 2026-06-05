from importlib.util import find_spec

from .training_config import load_training_config
from .training_artifacts import create_run_dir,write_training_artifacts
def plan_training(config_path,run_id=None,output_dir='experiments'):
 c=load_training_config(config_path); rd=create_run_dir(output_dir,run_id or c.get('run_id')); run={'run_id':rd.name,'model':c['model'],'dataset':c['dataset'],'dry_run':True,'artifacts_dir':str(rd)}; art=write_training_artifacts(rd,c,{'status':'planned','train_steps':0},run); return {'status':'planned','run_id':rd.name,'artifacts':art,'config':c}
def run_training(config_path,dry_run=True,run_id=None):
 if dry_run: return plan_training(config_path,run_id=run_id)
 if find_spec("torch") is None or find_spec("unsloth") is None:
  from .errors import TrainingError
  raise TrainingError('Real training requires torch, unsloth, model files, and a GPU environment')
 return plan_training(config_path,run_id=run_id)|{'status':'completed'}
