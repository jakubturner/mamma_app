import asyncio
import os
from configparser import ConfigParser

from dotenv import load_dotenv

from mamma_app.app import MammaApp


async def get_config() -> dict[str, str, int]:
    load_dotenv()
    config = ConfigParser()
    config.read("config.ini")

    url = config["DEFAULT"]["url"]
    api_token = os.getenv("API_TOKEN")
    api_limit = int(config["DEFAULT"]["api_limit"])
    # return url, api_token, api_limit
    config = config["DEFAULT"]
    data = {"url": url, "api_token": api_token, "api_limit": api_limit}
    return data


class App:
    def __init__(self):
        self.config = None
        load_dotenv()
        self.mamma_app = MammaApp()
        # self.config = ConfigParser()
        # self.conf = self.config.read("config.ini")
        self.url = None
        self.api_token = None
        self.api_limit = None

    async def setup(self) -> None:
        await self.mamma_app.setup_services(self.api_token, self.url)
        await self.mamma_app.configure_routes()
        # self.url = await self.config["DEFAULT"]["url"]
        # self.api_token = await os.getenv("API_TOKEN")
        # self.api_limit = await int(self.config["DEFAULT"]["api_limit"])
        self.api_token = "AHroaisT187U2Sm9xqYVH4OFlKddvSqKVy3GzRFL"
        self.url = "https://api.nasa.gov/neo/rest/v1/feed"
        self.api_limit = 7

        # print(self.config)

    async def run(self) -> None:
        await self.setup()

    async def close(self) -> None:
        # if self._channel is not None:
        #     await self._channel.aclose()
        ...


if __name__ == "__main__":
    app = App()
    asyncio.run(app.run())

# async def async_main() -> None:
#     app = App()
#     try:
#         await app.run()
#     except (Exception, KeyboardInterrupt) as e:  # pylint: disable=broad-except
#         pass
#     finally:
#         await app.close()
