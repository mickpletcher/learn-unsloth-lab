$ErrorActionPreference = 'Stop'
python -c "from learn_unsloth_lab.experiment_store import connect; connect('experiments/experiments.sqlite').close(); print('experiments/experiments.sqlite initialized')"
