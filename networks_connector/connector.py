from aiohttp.helpers import proxies_from_env
from logging import getLogger
from typing import Dict

from networks_connector.adapters.channels import VkAdapter, FacebookAdapter
from networks_connector.adapters.adapter import Adapter
from networks_connector.consts import VK_TOKEN, FACEBOOK_TOKEN


logger = getLogger("social_networks_connector")


class SocialNetworksConnector:
    adapters: Dict[str, Adapter]

    def __new__(cls, proxy: bool = False):
        if not hasattr(cls, "instance"):
            cls.instance = super(SocialNetworksConnector, cls).__new__(cls)
        cls.adapters = {
            "vk": VkAdapter(token=VK_TOKEN, proxy=proxy),
            "facebook": FacebookAdapter(token=FACEBOOK_TOKEN, proxy=proxy)
        }
        if proxy:
            proxies = proxies_from_env()
            if proxies:
                logger.info(f"Using HTTP proxy, details: {proxies}")
            else:
                logger.warning("Missing HTTP_PROXY env variable, proxy is inactive")
        return cls.instance

    async def get_user_info(self, channel: str, user: str):
        logger.info(f"Fetching user '{user}' {channel} page info")
        adapter = self.adapters.get(channel)
        return await adapter.get_profile(user=user)

    async def get_user_friends(self, channel: str, user: str):
        logger.info(f"Fetching user '{user}' {channel} page friends")
        adapter = self.adapters.get(channel)
        return await adapter.get_friends(user=user)

    async def get_user_wall(self, channel: str, user: str):
        logger.info(f"Fetching user '{user}' {channel} page wall")
        adapter = self.adapters.get(channel)
        return await adapter.get_wall(user=user)