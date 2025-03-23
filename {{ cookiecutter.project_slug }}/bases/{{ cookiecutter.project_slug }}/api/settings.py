from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from {{ cookiecutter.project_slug }}.persistence.rdb.settings import DatabaseSettings

APP_ROOT = Path(__file__).parent.parent

ENV_FILES = (APP_ROOT / '.env', APP_ROOT / 'local.env')

WebServer = Literal['uvicorn', 'granian']


class APISettings(BaseSettings):
    web_server: WebServer = 'uvicorn'
    database: DatabaseSettings = DatabaseSettings()

    model_config = SettingsConfigDict(
        env_file=ENV_FILES,
        env_nested_delimiter='__',
        extra='ignore',
    )
