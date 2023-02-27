import pytest
from starlette.testclient import TestClient

from mamma_app.app import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client