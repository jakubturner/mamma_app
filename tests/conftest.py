import json

import pytest
from starlette.testclient import TestClient

from mamma_app.app import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture()
def fake_data():
    with open("../tests/resources/data.json") as f:
        return json.load(f)
