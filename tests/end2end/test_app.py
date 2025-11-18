from fastapi.testclient import TestClient

from atlas.app.app import app

client = TestClient(app)


def test_main() -> None:
    response = client.get("/main")
    assert response.status_code == 200
    assert response.json() == {"result": "success!"}
