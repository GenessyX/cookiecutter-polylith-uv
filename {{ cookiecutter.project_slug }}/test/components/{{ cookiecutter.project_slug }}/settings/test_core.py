from {{ cookiecutter.project_slug }}.settings import core

def test_sample() -> None:
    assert core is not None
