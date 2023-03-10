import datetime

import pytest as pytest
from aioresponses import aioresponses
from starlette.testclient import TestClient

from mamma_app.app import app, get_config
from mamma_app.neo_ws_service import get_earth_objects

client = TestClient(app)


def test_root_endpoint(test_app) -> None:
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello there"}


# @pytest.mark.asyncio
# async def test_get_data():
#     with aioresponses() as m:
#         start_date = datetime.date(2022, 12, 1)
#         end_date = datetime.date(2022, 12, 1)
#         url, api_token, api_limit = await get_config()
#         m.get(f"{url}?start_date={start_date}&end_date={end_date}&api_key={api_token}", payload=dict(foo='bar'))
#         result = await get_data(api_token=api_token, url=url, start_date=start_date, end_date=end_date)
#
#         m.assert_called_once_with('http://test.example.com')
