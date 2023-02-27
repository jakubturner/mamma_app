from starlette.testclient import TestClient

from mamma_app.app import app

client = TestClient(app)


def test_root_endpoint(test_app) -> None:
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello there"}

