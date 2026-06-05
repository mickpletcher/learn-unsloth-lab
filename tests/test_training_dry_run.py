from learn_unsloth_lab.training import run_training
def test_training_dry_run_writes_artifacts():
 r=run_training('configs/example-training.yaml',dry_run=True,run_id='test-run')
 assert r['status']=='planned' and 'metrics' in r['artifacts']
