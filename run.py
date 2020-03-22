from fastapi import FastAPI, Depends
from app.config import config
from Apis.kr.CjLogistics import CjLogistics
from fastapi_plugins import redis_plugin, depends_redis
from aioredis import Redis
from app.util import timestamp
import typing

app = FastAPI(
    debug=True,
    title="Delivery API",
    description="배송 조회 API",
    version="dev 1.0"
)


@app.get("/")
async def root_get(cache: Redis = Depends(depends_redis), ) -> typing.Dict:
    stamp = await timestamp.stamp()
    return {"timestamp": stamp}

@app.get("/{track_id}")
async def root_get(track_id: str ,cache: Redis = Depends(depends_redis), ) -> typing.Dict:
    so = CjLogistics()
    return await so.GetCsrfCode(track_id=track_id)

@app.on_event('startup')
async def on_startup() -> None:
    await redis_plugin.init_app(app, config=config)
    await redis_plugin.init()


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await redis_plugin.terminate()