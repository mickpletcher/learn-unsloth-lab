from learn_unsloth_lab.dataset_conversion import convert_to_jsonl
def test_convert_alpaca_to_jsonl(tmp_path):
 out=tmp_path/'out.jsonl'; r=convert_to_jsonl('datasets/alpaca-sample.json',out)
 assert r['output_records']==10 and len(out.read_text().splitlines())==10
