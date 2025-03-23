from pathlib import Path
import shutil
import sys
import subprocess
import logging
from typing import cast

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def setup_repository() -> None:
    try:
        result = subprocess.run(["git", "init"], capture_output=True, check=True)
        logger.info("Set up repository: %s", result.stdout.decode("utf-8"))
        subprocess.run(
            ["git", "config", "user.email", "{{ cookiecutter.author_email }}"],
            capture_output=True,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "{{ cookiecutter.author }}"],
            capture_output=True,
            check=True,
        )
    except Exception:
        logger.exception("Failed to set up repository")
        sys.exit(1)


def setup_dependencies() -> None:
    try:
        subprocess.run(["uv", "sync", "--all-groups"])
        logger.info("Successfuly synced dependencies")
    except Exception:
        logger.exception("Failed to sync dependencies")
        sys.exit(1)


def setup_pre_commit() -> None:
    try:
        result = subprocess.run(
            ["uv", "run", "pre-commit", "install"],
            capture_output=True,
            check=True,
        )
        logger.info("Set up basic pre-commit hooks: %s", result.stdout.decode("utf-8"))
        result = subprocess.run(
            ["uv", "run", "pre-commit", "install", "--hook-type", "commit-msg"],
            capture_output=True,
            check=True,
        )
        logger.info(
            "Set up commit-msg pre-commit hooks: %s", result.stdout.decode("utf-8")
        )

    except Exception:
        logger.exception("Failed to set up pre-commit hooks")
        sys.exit(1)


def produce_first_commit() -> None:
    try:
        result = subprocess.run(["git", "add", "."], capture_output=True, check=True)
        logger.info(
            "Added all files to first commit: %s", result.stdout.decode("utf-8")
        )
        result = subprocess.run(
            ["uv", "run", "pre-commit", "run", "--all-files"],
            capture_output=True,
            check=False,
        )
        logger.info("Ran pre-commit on repo: %s", result.stdout.decode("utf-8"))
        result = subprocess.run(["git", "add", "."], capture_output=True, check=True)
        logger.info(
            "Added all files to first commit: %s", result.stdout.decode("utf-8")
        )
        result = subprocess.run(
            ["git", "commit", "-m", "chore: first commit"],
            capture_output=True,
            check=True,
        )
        logger.info("Produced first commit: %s", result.stdout.decode("utf-8"))
    except subprocess.CalledProcessError as err:
        logger.exception(
            "Failed to produce first commit: \n"
            + cast(bytes, err.stderr).decode("utf-8")
        )
        sys.exit(1)

sample_project_enabled = {% if cookiecutter.sample_project %} True {% else %} False {% endif %}
persistence_component_enabled = {% if cookiecutter.persistence_component %} True {% else %} False {% endif %}


def setup_local_env() -> None:
    if sample_project_enabled:
        with Path("bases/{{ cookiecutter.project_slug }}/api/local.env").open("w"):
            pass

def rm_sample_components() -> None:
    if not sample_project_enabled:
        shutil.rmtree(Path("bases/{{ cookiecutter.project_slug }}/api"))
        shutil.rmtree(Path("projects/{{ cookiecutter.project_slug }}/api"))
    if not persistence_component_enabled:
        shutil.rmtree( Path("components/{{ cookiecutter.project_slug }}/persistence"))
    if not sample_project_enabled and not persistence_component_enabled:
        shutil.rmtree(Path("components/{{ cookiecutter.project_slug }}/settings"))

if __name__ == "__main__":
    setup_repository()
    setup_dependencies()
    setup_pre_commit()
    rm_sample_components()
    produce_first_commit()
    setup_local_env()