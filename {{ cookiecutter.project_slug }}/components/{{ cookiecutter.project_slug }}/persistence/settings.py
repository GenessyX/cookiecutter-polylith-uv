import datetime
from dataclasses import dataclass

from pydantic import AnyUrl

from {{ cookiecutter.project_slug }}.settings.base import DbScheme, DsnSettings


@dataclass(kw_only=True)
class DatabaseSettings(DsnSettings):
    scheme: DbScheme = 'postgresql+asyncpg'  # pyright: ignore[reportIncompatibleVariableOverride]
    path: str = 'postgres'
    host: str = 'localhost'
    port: int = 5432
    echo: bool = False
    echo_pool: bool = False
    pool_pre_ping: bool = True
    pool_recycle: datetime.timedelta = datetime.timedelta(hours=1)
    pool_size: int = 20
    max_overflow: int = 10
    password: str = 'password'  # noqa: S105
    user: str = 'postgres'
    schema: str = 'public'

    @property
    def sync_dsn(self) -> AnyUrl:
        return AnyUrl.build(
            scheme='postgresql',
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            path=self.path,
        )
