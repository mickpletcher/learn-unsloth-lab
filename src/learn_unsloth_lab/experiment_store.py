from pathlib import Path
import json,sqlite3
from datetime import datetime,timezone
SCHEMA="""CREATE TABLE IF NOT EXISTS experiments(id INTEGER PRIMARY KEY,run_id TEXT UNIQUE,model_name TEXT,dataset_name TEXT,config_path TEXT,config_json TEXT,metrics_json TEXT,status TEXT,notes TEXT,created_at TEXT,updated_at TEXT);CREATE TABLE IF NOT EXISTS artifacts(id INTEGER PRIMARY KEY,run_id TEXT,kind TEXT,path TEXT);CREATE TABLE IF NOT EXISTS exports(id INTEGER PRIMARY KEY,run_id TEXT,path TEXT);"""
def connect(db_path='experiments/experiments.sqlite'):
 p=Path(db_path); p.parent.mkdir(parents=True,exist_ok=True); c=sqlite3.connect(p); c.row_factory=sqlite3.Row; c.executescript(SCHEMA); return c
def create_experiment(db_path,run_id,model_name,dataset_name,config_path='',config=None,notes=''):
 now=datetime.now(timezone.utc).isoformat()
 with connect(db_path) as c: c.execute('INSERT INTO experiments(run_id,model_name,dataset_name,config_path,config_json,status,notes,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)',(run_id,model_name,dataset_name,config_path,json.dumps(config or {}),'planned',notes,now,now))
 return run_id
def update_status(db_path,run_id,status):
 with connect(db_path) as c: c.execute('UPDATE experiments SET status=?,updated_at=? WHERE run_id=?',(status,datetime.now(timezone.utc).isoformat(),run_id))
def add_metrics(db_path,run_id,metrics):
 with connect(db_path) as c: c.execute('UPDATE experiments SET metrics_json=?,updated_at=? WHERE run_id=?',(json.dumps(metrics),datetime.now(timezone.utc).isoformat(),run_id))
def add_artifact(db_path,run_id,kind,path):
 with connect(db_path) as c: c.execute('INSERT INTO artifacts(run_id,kind,path) VALUES(?,?,?)',(run_id,kind,path))
def add_export(db_path,run_id,path):
 with connect(db_path) as c: c.execute('INSERT INTO exports(run_id,path) VALUES(?,?)',(run_id,path))
def list_experiments(db_path):
 with connect(db_path) as c: return [dict(r) for r in c.execute('SELECT * FROM experiments ORDER BY created_at DESC')]
def get_experiment(db_path,run_id):
 with connect(db_path) as c:
  r=c.execute('SELECT * FROM experiments WHERE run_id=?',(run_id,)).fetchone(); return dict(r) if r else None
