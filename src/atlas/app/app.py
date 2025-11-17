from fastapi import FastAPI

from atlas.app.routers.artist import artist_router
from atlas.config.fast_api import fast_api_settings

app = FastAPI(**fast_api_settings.model_dump())

app.include_router(artist_router)


@app.get("/main")
def main() -> dict[str, str]:
    return {"result": "success!"}
