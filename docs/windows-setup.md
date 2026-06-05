# Windows Setup

Use PowerShell from the repository root.

## Open The Repo

```powershell
cd "C:\Users\mick0\OneDrive\Documents\Code & Dev\GitHub\learn-unsloth-lab"
```

The quotes matter because the path contains spaces and `&`.

## Create A Virtual Environment

```powershell
py -3.11 -m venv .venv
```

## Activate It

```powershell
.\.venv\Scripts\Activate.ps1
```

Expected prompt behavior:

```text
(.venv) PS C:\Users\mick0\OneDrive\Documents\Code & Dev\GitHub\learn-unsloth-lab>
```

## Install The Lab

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

## Install Developer Tools

```powershell
python -m pip install -e .[dev]
```

## Verify

```powershell
python -m learn_unsloth_lab --help
python -m pytest
python -m ruff check .
```

If script execution is blocked, set the current user policy:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
