from pathlib import Path
import json
from .dataset_formats import ALLOWED_ROLES,normalize_record
from .errors import DatasetError
def read_records(path):
    p=Path(path)
    if not p.exists(): raise DatasetError(f'Dataset not found: {p}')
    txt=p.read_text(encoding='utf-8').strip()
    if not txt: raise DatasetError('Dataset is empty')
    if p.suffix=='.jsonl': return [json.loads(x) for x in txt.splitlines() if x.strip()]
    data=json.loads(txt)
    if isinstance(data,list): return data
    if isinstance(data,dict) and isinstance(data.get('data'),list): return data['data']
    raise DatasetError('JSON dataset must be a list or data list')
def validate_messages(m):
    e=[]
    if not m: e.append('record has no messages')
    if not any(x.get('role')=='assistant' for x in m): e.append('record has no assistant reply')
    for i,x in enumerate(m):
        if x.get('role') not in ALLOWED_ROLES: e.append(f'message {i} has invalid role')
        if not str(x.get('content','')).strip(): e.append(f'message {i} has blank content')
    return e
def validate_records(records):
    errs=[]
    for i,r in enumerate(records):
        try: es=validate_messages(normalize_record(r)['messages'])
        except Exception as ex: es=[str(ex)]
        errs += [{'index':i,'error':x} for x in es]
    return {'valid':not errs,'record_count':len(records),'errors':errs}
def validate_dataset(path): return validate_records(read_records(path))
