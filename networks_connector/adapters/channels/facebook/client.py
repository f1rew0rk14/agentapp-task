from networks_connector.adapters.channels.aio_client import Client


class FacebookClient(Client):
    def __init__(self, token: str, proxy: bool = False):
        super(FacebookClient, self).__init__(proxy)
        self.token = token

    async def get_user(self, user_id: int, fields):
        url = f"https://graph.facebook.com/v12.0/{user_id}"
        params = {
            "access_token": self.token,
            "fields": ",".join(fields)
        }
        return await self.get(url=url, params=params)

    async def get_friends(self, user_id: int, fields: list):
        url = f"https://graph.facebook.com/v12.0/{user_id}/friends"
        params = {
            "access_token": self.token,
            "fields": ",".join(fields)
        }
        return await self.get(url=url, params=params)

    async def get_feed(self, user_id: int):
        url = f"https://graph.facebook.com/v12.0/{user_id}/feed"
        params = {
            "access_token": self.token,
        }
        return await self.get(url=url, params=params)
