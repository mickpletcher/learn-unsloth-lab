from learn_unsloth_lab.experiment_reports import write_experiment_summary
from learn_unsloth_lab.experiment_store import create_experiment
def test_experiment_report(tmp_path):
 db=tmp_path/'x.sqlite'; create_experiment(db,'run1','model','dataset')
 assert write_experiment_summary(db,tmp_path)['markdown'].endswith('experiments-summary.md')
