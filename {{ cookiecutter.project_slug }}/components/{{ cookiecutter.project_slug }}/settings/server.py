from dataclasses import dataclass


@dataclass(kw_only=True)
class ServerSettings:
    port: int = 8000
    host: str = "127.0.0.1"
    workers: int = 1
    openapi_url: str = "/openapi.json"
