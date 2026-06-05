from learn_unsloth_lab.evaluation_metrics import adherence_score,response_length,similarity_score
def test_metrics():
 assert response_length('one two')==2
 assert similarity_score('alpha beta','alpha gamma')>0
 assert adherence_score('Explain budget variance','Budget variance is the gap')>0
