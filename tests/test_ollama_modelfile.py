from learn_unsloth_lab.ollama import generate_modelfile
def test_modelfile():
 text=generate_modelfile({'gguf_path':'model.gguf','model_name':'x','parameters':{'temperature':0.2}})
 assert 'FROM model.gguf' in text and 'PARAMETER temperature 0.2' in text
