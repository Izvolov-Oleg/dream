from typing import Optional

from aiohttp import ClientSession, TCPConnector


class ServiceClient:

    def __init__(self, service_url: str):
        self.url = service_url

    def get_url(self, endpoint: str) -> str:
        return self.url + endpoint

    async def get_data_from_service(self, payload: Optional[dict] = None) -> list:
        url = self.get_url('badlisted_words')
        async with ClientSession(connector=TCPConnector(ssl=False)) as session:
            async with session.post(url, json=payload) as resp:
                return await resp.json()
