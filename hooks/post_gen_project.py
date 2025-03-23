import sys
import subprocess
import logging

logger = logging.getLogger(__name__)


def setup_repository() -> None:
    try:
        result = subprocess.run(["git", "init"], capture_output=True, check=True)
        logger.info("Set up repository: %s", result.stdout.decode("utf-8"))
    except Exception:
        logger.exception("Failed to set up repository")
        sys.exit(1)


def setup_dependencies() -> None:
    try:
        result = subprocess.run(["uv", "sync", "--all-groups"])
        print(result)
        print(result.stdout)
        print(result.stderr)
        logger.info("Synced dependencies: %s", result.stdout.decode("utf-8"))
    except Exception:
        logger.exception("Failed to sync dependencies")
        sys.exit(1)


def setup_pre_commit() -> None:
    try:
        result = subprocess.run(
            ["uv", "run", "pre-commit", "install"], capture_output=True, check=True
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


if __name__ == "__main__":
    setup_repository()
    setup_dependencies()
    setup_pre_commit()
