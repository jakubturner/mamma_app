import datetime
import os
from typing import Optional

from fastapi import FastAPI, HTTPException, status

from mamma_app.model import EarthObjectParsed
from mamma_app.neo_ws_service import get_data
from configparser import ConfigParser
from dotenv import load_dotenv

app = FastAPI()


async def get_config() -> tuple[str, str]:
    load_dotenv()
    api_token = os.getenv("API_TOKEN")
    config = ConfigParser()
    config.read("config.ini")
    url = config["DEFAULT"]["url"]
    return url, api_token


@app.get("/")
async def root():
    return {"message": "Test app for mamma.ai"}


@app.get("/objects", status_code=status.HTTP_200_OK)
async def get_objects(start_date: Optional[datetime.date] = datetime.datetime.today().date(),
                      end_date: Optional[datetime.date] = datetime.datetime.today().date()) -> list[EarthObjectParsed]:
    url, api_token = await get_config()
    data = await get_data(url, start_date, end_date, api_token)
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="Data does not found")
    return data
