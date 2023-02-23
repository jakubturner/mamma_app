import datetime
import json

from aiohttp import ClientSession

from mamma_app.model import EarthObject, EarthObjectParsed


async def get_data(url: str, start_date: datetime.date, end_date: datetime.date, api_key: str) -> list[EarthObjectParsed]:
    async with ClientSession() as session:
        async with session.get(url=f"{url}?start_date={start_date}&end_date={end_date}&api_key={api_key}") as response:
            response = await response.read()
            data = json.loads(response)
            items = []

            for date, _ in data["near_earth_objects"].items():
                for earth_object in _:
                    try:
                        e_object = EarthObject.parse_obj(earth_object)
                        for close_apr_data in e_object.close_approach_data:
                            parsed_object = EarthObjectParsed(name=e_object.name,
                                                              size_estimate=e_object.estimated_diameter.kilometers,
                                                              time=close_apr_data.close_approach_date_full,
                                                              distance=close_apr_data.miss_distance.kilometers)
                        items.append(parsed_object)
                    except Exception:
                        pass
            return sorted(items, key=lambda x: x.distance)
