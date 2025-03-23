from {{ cookiecutter.project_slug }}.api.settings import APISettings

settings = APISettings()


if __name__ == "__main__":
    if settings.web_server == "granian":
        from granian.constants import Interfaces, Loops
        from granian.server import Server

        runtime = Server(
            "{{ cookiecutter.project_slug }}.api.core:app",
            reload=settings.app.reload,
            port=settings.server.port,
            address=settings.server.host,
            loop=Loops.uvloop,
            interface=Interfaces.ASGI,
            workers=settings.server.workers,
        )
        runtime.serve()

    if settings.web_server == "uvicorn":
        import uvicorn

        uvicorn.run(
            "{{ cookiecutter.project_slug }}.api.core:app",
            reload=settings.app.reload,
            port=settings.server.port,
            host=settings.server.host,
        )
