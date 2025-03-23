from typing import TYPE_CHECKING

from sqlalchemy.orm import registry

mapper_registry = registry()

if TYPE_CHECKING:
    from sqlalchemy.sql.schema import Column
else:
    from sqlalchemy.sql.schema import Column as _Column

    class Column(_Column):
        inherit_cache = True

        def __init__(self, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
            kwargs.setdefault('nullable', False)
            super().__init__(*args, **kwargs)


__all__ = ['Column']
