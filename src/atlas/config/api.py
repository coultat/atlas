from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ConfigDict, Field
from functools import lru_cache
from atlas.config.path import BASE_DIR


class AtlasApi(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/default.env",
        env_file_encoding="utf-8",
        env_prefix="ATLAS_API_",
        extra="ignore",
        case_sensitive=False
    )

    api_title: str = Field(alias="title", default="Default API Name", env="ATLAS_API_NAME")
    description: str = Field(
        default="API for Atlas application. This will play around with the Spotify API and databases.",
        env="DESCRIPTION"
    )
    docs_url: str = Field(default="/", env="DOCS_URL")
    openapi_url: str = Field(default="/openapi.json", env="OPENAPI_URL")
    redirect_slashes: bool = True
       
    
@lru_cache()
def get_settings() -> AtlasApi:
    return AtlasApi()
    
    
fast_api_settings = get_settings()