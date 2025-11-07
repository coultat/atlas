from fastapi import FastAPI

app = FastAPI(docs_url="/", title="Atlas API", description="API for Atlas application")

@app.get("/main")
def main():
    return {"result": "success!"}
