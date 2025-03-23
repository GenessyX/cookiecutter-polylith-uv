import logging
import subprocess
import sys

logger = logging.getLogger(__name__)


def is_uv_installed() -> None:
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, check=True)
        logger.info("uv version installed: %s", result.stdout.decode("utf-8"))
    except Exception:
        logger.exception("Check if `uv` is installed")
        sys.exit(1)


if __name__ == "__main__":
    is_uv_installed()
