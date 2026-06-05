from learn_unsloth_lab.hyperparameters import plan_sweep
from learn_unsloth_lab.hyperparameter_reports import write_sweep_report
def test_sweep_report(tmp_path): assert 'html' in write_sweep_report(plan_sweep('configs/hyperparameter-sweep.yaml',tmp_path/'sweeps'),tmp_path)
