import datetime
from typing import Optional

from fastapi import FastAPI

from mamma_app.neo_ws_service import get_data
from configparser import ConfigParser

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Test app for mamma.ai"}


@app.get("/objects")
async def get_objects(start_date: Optional[datetime.date] = None, end_date: Optional[datetime.date] = None):
    config = ConfigParser()
    config.read("config.ini")
    url = config["DEFAULT"]["url"]
    api_token = config["DEFAULT"]["api_token"]

    data = await get_data(url, start_date, end_date, api_token)
    # print(data["data"]["near_earth_objects"])
    return data["data"]["near_earth_objects"]
