from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import FrozenSet

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str = "5836801048:AAHrAtSk4LuGMQlITBn6Q3Cz91HxL_1mv94"
    admin_ids: FrozenSet[int] = frozenset({731704647})


settings = Settings()
