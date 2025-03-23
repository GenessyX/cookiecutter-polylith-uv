# {{ cookiecutter.project_name }}

{%- if cookiecutter.sample_project %}
## project run

uvicorn:
```bash
uv run python projects/api/run.py
```
granian:
```bash
WEB_SERVER=granian uv run python projects/api/run.py
```
{%- endif %}

## project build

```bash
cd projects/{project_name}
uv build --wheel
```

## pre-commit

```bash
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
```

## coverage

```bash
uv run poe html-cov
```
