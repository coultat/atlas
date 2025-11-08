from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from atlas.config.path import BASE_DIR


class AtlasApi(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/default.env",
        env_file_encoding="utf-8",
        env_prefix="ATLAS_API_",
        extra="ignore",
        case_sensitive=False,
    )

    api_title: str = Field(
        alias="title", default="Default API Name", validation_alias="ATLAS_API_NAME"
    )  # title has a bug reading with env_prefix, that's why the alias
    description: str = Field(alias="description",
        default="API for Atlas application. This will play around with the Spotify API and databases.",
        validation_alias="DESCRIPTION",
    )
    docs_url: str = Field(alias="docs_url",default="/", validation_alias="DOCS_URL")
    openapi_url: str = Field(default="/openapi.json", validation_alias="OPENAPI_URL")
    redirect_slashes: bool = True


@lru_cache()
def get_settings() -> AtlasApi:
    return AtlasApi()


fast_api_settings = get_settings()
