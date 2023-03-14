import datetime
import itertools
import json
import math
from typing import Optional, List
import aiohttp
import asyncio

from mamma_app.model import EarthObject, EarthObjectParsed


class EarthObjectAPI:
    def __init__(self, api_token: str, url: str):
        self.api_token = api_token
        self.url = url

    async def get_earth_objects_in_time_range(
            self,
            api_limit: int,
            start_date: datetime.date,
            end_date: datetime.date
    ) -> List[EarthObjectParsed]:
        num_days = (end_date - start_date).days
        coroutines = []

        if num_days < api_limit:
            results = await self.get_earth_objects(start_date=start_date, end_date=end_date)
            return sorted(results)

        for i in range(math.ceil(num_days / api_limit)):
            st_date = start_date + datetime.timedelta(days=i * api_limit)
            en_date = st_date + datetime.timedelta(days=api_limit)

            coroutines.append(
                self.get_earth_objects(start_date=st_date, end_date=min([end_date, en_date]))
            )

        results = list(itertools.chain(*await asyncio.gather(*coroutines, return_exceptions=True)))
        return sorted(results)

    async def get_earth_objects(
            self,
            start_date: datetime.date,
            end_date: datetime.date
    ) -> List[Optional[EarthObjectParsed]]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        url=f"{self.url}?start_date={start_date}&end_date={end_date}&api_key={self.api_token}"
                ) as response:
                    response = await response.read()
                    data = json.loads(response)
                    items = []

                    for date, _ in data["near_earth_objects"].items():
                        for earth_object in _:
                            try:
                                e_object = EarthObject.parse_obj(earth_object)
                                for close_apr_data in e_object.close_approach_data:
                                    parsed_object = EarthObjectParsed(
                                        name=e_object.name,
                                        size_estimate=e_object.estimated_diameter.kilometers,
                                        time=close_apr_data.close_approach_date_full,
                                        distance=close_apr_data.miss_distance.kilometers,
                                    )
                                    items.append(parsed_object)
                            except Exception as e:
                                print(e)
                                # continue with the next object
                                pass
                    return items
        except aiohttp.ClientError:
            print("Error: Could not retrieve data from API")
            return []
