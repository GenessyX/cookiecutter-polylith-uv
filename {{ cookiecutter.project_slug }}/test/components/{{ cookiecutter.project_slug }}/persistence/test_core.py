from {{ cookiecutter.project_name }}.persistence import core

def test_sample() -> None:
    assert core is not None
