from dataclasses import dataclass
from typing import Literal

from pydantic import AnyUrl

DbScheme = Literal['postgresql', 'postgresql+psycopg2', 'postgresql+asyncpg', 'sqlite']
HttpScheme = Literal['http']
BrokerScheme = Literal['amqp', 'kafka']
KVScheme = Literal['redis', 'memcached']
SmtpScheme = Literal['smtp']

ValidScheme = DbScheme | HttpScheme | BrokerScheme | KVScheme | SmtpScheme


@dataclass(kw_only=True)
class DsnSettings:
    host: str = 'localhost'
    port: int = 1337
    user: str = ''
    password: str = ''
    scheme: ValidScheme = 'http'
    path: str = ''

    @property
    def dsn(self) -> AnyUrl:
        return AnyUrl.build(
            scheme=self.scheme,
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            path=self.path,
        )
