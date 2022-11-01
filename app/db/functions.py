from app.db import engine
from app.db.models import privileges, users, chats


memory = {}


async def commit(instance):
    """commit instance"""
    conn = await engine.connect()

    result = await conn.execute(instance)
    await conn.commit()
    await conn.close()
    return result


async def get_or_create(model, **kwargs):
    """add string to db"""
    query = await get(model, **kwargs)

    if query:
        return query
    else:
        ins = model.insert().values(**kwargs)
        await commit(ins)
        return await get(model, **kwargs)


async def get(model, **kwargs):
    """check string in db"""
    conn = await engine.connect()

    s = model.select().filter_by(**kwargs)
    query = (await conn.execute(s)).all()
    await conn.close()
    return query
