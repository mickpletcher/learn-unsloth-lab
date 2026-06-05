from itertools import product
from pathlib import Path
from .config import load_yaml_config,write_yaml
from .training import run_training
def expand_sweep(c):
 vals=c['sweep']; keys=['lora_rank','lora_alpha','learning_rate','epochs','batch_size','sequence_length']; runs=[dict(zip(keys,x,strict=True)) for x in product(*(vals[k] for k in keys))]
 if len(runs)>c.get('max_runs',50): raise ValueError('Sweep expands above max_runs')
 return runs
def plan_sweep(config_path,output_root='experiments/sweeps'):
 c=load_yaml_config(config_path); sid=c.get('sweep_id','default-sweep'); o=Path(output_root)/sid; o.mkdir(parents=True,exist_ok=True); runs=[]
 for i,combo in enumerate(expand_sweep(c),1):
  resolved=c['base_config']|{'training':c['base_config'].get('training',{})|combo}; p=write_yaml(o/f'run-{i:03d}.yaml',resolved); runs.append({'run':i,'config':str(p),'parameters':combo})
 return {'sweep_id':sid,'run_count':len(runs),'runs':runs}
def execute_sweep(config_path,dry_run=True): return [run_training(r['config'],dry_run=dry_run) for r in plan_sweep(config_path)['runs']]
