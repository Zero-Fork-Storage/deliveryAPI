from fastapi import FastAPI, Depends
from app.config import config
from fastapi_plugins import redis_plugin, depends_redis
from app.core.carriers.kr.CjLogistics import CjLogistics
from app.models.jsonModel import ResponseModel
from aioredis import Redis
from app.core import Routing
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
async def track_get(track_id, cache: Redis = Depends(depends_redis), ) -> typing.Dict:
    source = Routing()
    one = await source.excute(track_id=track_id)
    return one


@app.on_event('startup')
async def on_startup() -> None:
    await redis_plugin.init_app(app, config=config)
    await redis_plugin.init()


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await redis_plugin.terminate()