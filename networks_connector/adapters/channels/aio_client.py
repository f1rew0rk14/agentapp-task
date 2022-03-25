from typing import Dict, Optional
from aiohttp import ClientSession


class Client:
    def __init__(self, proxy: bool = False):
        self._proxy_mode = proxy

    async def get(self, url: str, params: Optional[Dict] = None) -> Dict:
        async with ClientSession(trust_env=self._proxy_mode) as session:
            async with session.get(
                url=url,
                params=params
            ) as response:
                return await response.json()
