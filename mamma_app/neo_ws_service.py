import datetime
import json

from aiohttp import ClientSession


async def get_data(url: str, start_date: datetime.date, end_date: datetime.date, api_key: str):
    async with ClientSession() as session:
        async with session.get(url=f"{url}?start_date={start_date}&end_date={end_date}&api_key={api_key}") as response:
            response = await response.read()
            return {"data": json.loads(response)}
