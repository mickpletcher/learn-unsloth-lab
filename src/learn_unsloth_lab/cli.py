from pathlib import Path
import json, typer
from rich.console import Console
from rich.table import Table
from .dashboard import generate_dashboard
from .dataset_conversion import convert_to_jsonl
from .dataset_validation import validate_dataset
from .evaluation import run_evaluation
from .export import export_gguf
from .experiment_reports import write_experiment_summary
from .experiment_store import get_experiment,list_experiments
from .ollama import run_ollama
from .training import run_training
app=typer.Typer(help='Learn Unsloth Lab CLI'); dataset_app=typer.Typer(help='Dataset tools'); export_app=typer.Typer(help='Export tools'); ollama_app=typer.Typer(help='Ollama tools'); experiments_app=typer.Typer(help='Experiment tracking'); c=Console()
app.add_typer(dataset_app,name='dataset'); app.add_typer(export_app,name='export'); app.add_typer(ollama_app,name='ollama'); app.add_typer(experiments_app,name='experiments')
@dataset_app.command('validate')
def dataset_validate(path:Path):
 r=validate_dataset(path); c.print_json(json.dumps(r));
 if not r['valid']: raise typer.Exit(1)
@dataset_app.command('convert')
def dataset_convert(input_path:Path,output:Path): c.print_json(json.dumps(convert_to_jsonl(input_path,output)))
@app.command()
def train(config:Path,dry_run:bool=True): c.print_json(json.dumps(run_training(config,dry_run=dry_run),default=str))
@app.command()
def evaluate(prompts:Path,output:Path=Path('experiments/evaluation')): c.print_json(json.dumps(run_evaluation(prompts,output),default=str))
@export_app.command('gguf')
def export_gguf_cmd(config:Path,dry_run:bool=True): c.print_json(json.dumps(export_gguf(config,dry_run=dry_run),default=str))
@ollama_app.command('create')
def ollama_create(config:Path,dry_run:bool=True): c.print_json(json.dumps(run_ollama(config,dry_run=dry_run),default=str))
@experiments_app.command('list')
def experiments_list(db:Path=Path('experiments/experiments.sqlite')):
 t=Table('Run','Model','Dataset','Status')
 for r in list_experiments(db): t.add_row(r['run_id'],r['model_name'],r['dataset_name'],r['status'])
 c.print(t)
@experiments_app.command('show')
def experiments_show(run_id:str,db:Path=Path('experiments/experiments.sqlite')):
 r=get_experiment(db,run_id)
 if not r: raise typer.Exit(1)
 c.print_json(json.dumps(r))
@app.command()
def reports(db:Path=Path('experiments/experiments.sqlite'),output:Path=Path('experiments/reports')): c.print_json(json.dumps(write_experiment_summary(db,output)))
@app.command()
def dashboard(output:Path=Path('experiments/dashboard')): c.print_json(json.dumps(generate_dashboard(output_dir=output)))
def main(): app()
