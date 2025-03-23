from {{ cookiecutter.project_name }}.settings import core

def test_sample() -> None:
    assert core is not None
