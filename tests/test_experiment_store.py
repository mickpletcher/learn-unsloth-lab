from learn_unsloth_lab.experiment_store import add_artifact,add_metrics,create_experiment,get_experiment,list_experiments,update_status
def test_experiment_store(tmp_path):
 db=tmp_path/'x.sqlite'; create_experiment(db,'run1','model','dataset'); update_status(db,'run1','completed'); add_metrics(db,'run1',{'score':1}); add_artifact(db,'run1','log','log.txt')
 assert get_experiment(db,'run1')['status']=='completed' and len(list_experiments(db))==1
