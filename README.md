# cookiecutter-polylith-uv

Cookiecutter template with set up polylith repository.

## Usage

```bash
pipx run cookiecutter gh:genessyx/cookiecutter-polylith-uv
```

Answer the questions and ready to go.

## What is included

1. [Polylith repository](https://github.com/polyfy/polylith) with set up components, bases and projects directories using [`uv`](https://github.com/astral-sh/uv) package manager.
2. Initialized git repository with set up `user.name` and `user.email` configuration.
3. [`mypy`](https://github.com/python/mypy) for type checking with support for namespace packages (polylith structure).
4. [`pyright`](https://github.com/microsoft/pyright) or [`basedpyright`](https://github.com/DetachHead/basedpyright) (by default) set up to work with polylith-style repository.
5. [`ruff`](https://github.com/astral-sh/ruff) with almost all rules for static code analysis.
6. Installed [`pre-commit`](https://github.com/pre-commit/pre-commit) hooks:
    - [Basic hooks](https://github.com/pre-commit/pre-commit-hooks).
    - TOML formatter [taplo-format](https://github.com/ComPWA/taplo-pre-commit).
    - [`ruff` hook](https://github.com/astral-sh/ruff-pre-commit).
    - [`mypy` hook](https://github.com/pre-commit/mirrors-mypy).
    - [`commitlint` hook](https://github.com/alessandrojcm/commitlint-pre-commit-hook) set up with angular style commits.
7. License included:
    - GPL-3.0 (**default**) 
    - MIT 
    - Proprietary
8. Testing and coverage with [`pytest`](https://github.com/pytest-dev/pytest) and [`coverage`](https://github.com/nedbat/coveragepy).
9. Task runner [`poethepoet`](https://github.com/nat-n/poethepoet) with set up tasks for coverage (html) and poly check.
10. Optionally set up sample project named `api` with `Dockerfile` and `pyproject.toml` set up.
11. Optionally set up persistence component (`sqlalchemy`, `alembic`) + set up alembic directory in sample project `api`.
