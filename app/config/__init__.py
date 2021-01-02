import fastapi_plugins
import pydantic


class OtherSettings(pydantic.BaseSettings):
    other: str = 'other'


class AppSettings(OtherSettings, fastapi_plugins.RedisSettings):
    api_name: str = str(__name__)


config = AppSettings()
