from {{ cookiecutter.project_slug }}.api import core

def test_sample() -> None:
    assert core is not None
