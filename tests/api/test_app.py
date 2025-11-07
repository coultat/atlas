from fastapi.testclient import TestClient
from atlas.api.app import app


client = TestClient(app)


def test_main():
    response = client.get("/main")
    assert response.status_code == 200
    assert response.json() == {"result": "success!"}