import datetime
import os
from configparser import ConfigParser
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status

from mamma_app.model import EarthObjectParsed
from mamma_app.neo_ws_service import get_earth_objects_in_time_range

app = FastAPI()


async def get_config() -> tuple[str, str, int]:
    load_dotenv()
    config = ConfigParser()
    config.read("config.ini")

    url = config["DEFAULT"]["url"]
    api_token = os.getenv("API_TOKEN")
    api_limit = int(config["DEFAULT"]["api_limit"])
    return url, api_token, api_limit


@app.get("/")
async def root():
    return {"message": "hello there"}


@app.get("/objects", status_code=status.HTTP_200_OK)
async def get_objects(
    start_date: Optional[datetime.date] = datetime.datetime.today().date(),
    end_date: Optional[datetime.date] = datetime.datetime.today().date(),
) -> list[EarthObjectParsed]:
    url, api_token, api_limit = await get_config()
    data = await get_earth_objects_in_time_range(
        api_limit=api_limit, api_token=api_token, url=url, start_date=start_date, end_date=end_date
    )
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="Data does not found")
    return data
