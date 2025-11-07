from fastapi import FastAPI

from atlas.config.fast_api import fast_api_settings

app = FastAPI(**fast_api_settings.model_dump())


@app.get("/main")
def main() -> dict[str, str]:
    return {"result": "success!"}
