from learn_unsloth_lab.hyperparameters import plan_sweep
def test_sweep_expands(tmp_path): assert plan_sweep('configs/hyperparameter-sweep.yaml',tmp_path)['run_count']==8
