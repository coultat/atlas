from pydantic_settings import BaseSettings
from pydantic import ConfigDict, Field
from functools import lru_cache
from atlas.config.path import BASE_DIR


class AtlasApi(BaseSettings):
    model_config = ConfigDict(env_file=f"{BASE_DIR}default.env", env_file_encoding="utf-8")
    api_title: str = Field(default="Atlas API", validation_alias="ATLAS_API_NAME")
    api_description: str = "API for Atlas application. This will play around with the Spotify API and databases."
    api_docs_url: str = "/"
    api_openapi_url: str = "/openapi.json"
    api_redirect_slashes: bool = True
       
    
@lru_cache()
def get_settings() -> AtlasApi:
    return AtlasApi()
    
    
settings = get_settings()
print(settings.api_title)