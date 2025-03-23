from {{ cookiecutter.project_name }}.api import core

def test_sample() -> None:
    assert core is not None
