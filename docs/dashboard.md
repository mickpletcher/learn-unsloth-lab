# Dashboard

The dashboard is a static local HTML file.

It reads local project folders and summarizes:

- Datasets.
- Reports.
- Exports.
- Challenge files.

## Generate Dashboard

```powershell
python -m learn_unsloth_lab dashboard
```

Expected artifacts:

```text
experiments\dashboard\index.html
experiments\dashboard\dashboard-data.json
```

Open the HTML file in a browser.

## Fresh Repo Behavior

If no experiments or exports exist yet, the dashboard renders empty states. That is expected.

## Current Limits

The dashboard is static. It does not run a web server, require auth, or support multi user access.
