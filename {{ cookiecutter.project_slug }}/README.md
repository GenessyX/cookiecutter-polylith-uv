# {{ cookiecutter.project_name }}

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
