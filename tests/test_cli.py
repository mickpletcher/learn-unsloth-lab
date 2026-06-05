from typer.testing import CliRunner
from learn_unsloth_lab.cli import app
runner=CliRunner()
def test_cli_help():
 r=runner.invoke(app,['--help']); assert r.exit_code==0 and 'Learn Unsloth Lab CLI' in r.output
def test_dataset_validate_cli():
 r=runner.invoke(app,['dataset','validate','datasets/finance-instructions.jsonl']); assert r.exit_code==0
