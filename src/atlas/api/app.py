from fastapi import FastAPI
from atlas.config.api import fast_api_settings
app = FastAPI(**fast_api_settings.model_dump())

@app.get("/main")
def main():
    return {"result": "success!"}
