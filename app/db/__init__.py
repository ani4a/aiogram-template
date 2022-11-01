from sqlalchemy.ext.asyncio import create_async_engine

from app.config_parse import parser
from app.db.models import metadata


handlersList = []

engine = create_async_engine(
        parser()["db"]["url"],
        future=True,
        echo=False
)


async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
