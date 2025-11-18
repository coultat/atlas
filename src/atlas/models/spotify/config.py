from pydantic_settings import BaseSettings, SettingsConfigDict

from atlas.config.path import BASE_DIR


class SpotifyConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}default.env",
        env_file_encoding="utf-8",
        env_prefix="SPOTIFY_",
        extra="ignore",
        case_sensitive=False,
    )

    client_id: str
    secret: str


async def get_spotify_config() -> SpotifyConfig:
    return SpotifyConfig()  # type: ignore [call-arg]
