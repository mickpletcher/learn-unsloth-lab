# Hyperparameter Lab

The hyperparameter lab creates planned training configs for controlled experiments.

It sweeps:

- LoRA rank.
- LoRA alpha.
- Learning rate.
- Epochs.
- Batch size.
- Sequence length.

## Config

Use:

```text
configs\hyperparameter-sweep.yaml
```

The config includes `max_runs` to stop accidental large sweeps.

## Current Access Pattern

There is no CLI command for sweeps yet. Use the Python API:

```powershell
python -c "from learn_unsloth_lab.hyperparameters import plan_sweep; print(plan_sweep('configs/hyperparameter-sweep.yaml'))"
```

Expected artifact:

```text
experiments\sweeps\finance-small-sweep\run-001.yaml
```

## Current Limits

The lab plans sweeps and can call dry run training from Python. Full training execution is intentionally separate from the default offline workflow.
