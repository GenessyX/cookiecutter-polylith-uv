from dataclasses import dataclass
from enum import Enum


class AppStage(str, Enum):
    LOCAL = "local"
    TEST = "test"
    DEV = "dev"
    REVIEW = "review"
    STAGE = "stage"
    PRODUCTION = "production"


@dataclass(kw_only=True)
class AppSettings:
    name: str = "api"
    stage: AppStage = AppStage.LOCAL
    debug: bool = False
    reload: bool = True
