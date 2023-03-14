import asyncio
import datetime
import os
from configparser import ConfigParser
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status

from mamma_app.model import EarthObjectParsed
from mamma_app.neo_ws_service import EarthObjectAPI


# async def get_config() -> tuple[str, str, int]:
# async def get_config() -> dict[str, str, int]:
#     load_dotenv()
#     config = ConfigParser()
#     config.read("config.ini")
#
#     url = config["DEFAULT"]["url"]
#     api_token = os.getenv("API_TOKEN")
#     api_limit = int(config["DEFAULT"]["api_limit"])
#     # return url, api_token, api_limit
#     config = config["DEFAULT"]
#     data = {"url": url, "api_token": api_token, "api_limit": api_limit}
#     return data


class MammaApp:
    def __init__(self):
        self.app = FastAPI()
        self.neo_ws_service = None

    async def setup_services(self, api_token, url):
        # url, api_token, api_limit = await get_config()
        # self.neo_ws_service = EarthObjectAPI(api_limit=config["api_limit"], api_token=config["api_token"], url=config["url"])
        self.neo_ws_service = EarthObjectAPI(api_token=api_token, url=url)

    async def configure_routes(self):
        @self.app.get("/")
        async def root():
            return {"message": "hello there"}

        @self.app.get("/objects", status_code=status.HTTP_200_OK)
        async def get_objects(
                start_date: Optional[datetime.date] = datetime.datetime.today().date(),
                end_date: Optional[datetime.date] = datetime.datetime.today().date(),
        ) -> list[EarthObjectParsed]:
            if self.neo_ws_service is None:
                raise HTTPException(status_code=500, detail="Service is not set up yet")

            data = await self.neo_ws_service.get_earth_objects_in_time_range(
                start_date=start_date, end_date=end_date
            )

            if len(data) == 0:
                raise HTTPException(status_code=404, detail="Data not found")

            return data

    # async def start(self):
    #     await self.setup_services()
    #     self.configure_routes()
