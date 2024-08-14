from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str = "5836801048:AAHrAtSk4LuGMQlITBn6Q3Cz91HxL_1mv94"
    admin_ids: frozenset[int] = frozenset({42, 3595399})


settings = Settings()
