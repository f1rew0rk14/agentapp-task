from networks_connector.adapters.channels.aio_client import Client


class VkClient(Client):
    def __init__(self, token: str, proxy: bool = False):
        super(VkClient, self).__init__(proxy)
        self.token = token

    async def users_get(self, user_id: int, fields: list):
        url = (f"https://api.vk.com/method/users.get?user_ids={user_id}"
               f"&fields={','.join(fields)}&access_token={self.token}&v=5.122")
        return await self.get(url=url)

    async def friends_get(self, user_id: int, fields: list):
        url = (f"https://api.vk.com/method/friends.get?user_id={user_id}"
               f"&fields={','.join(fields)}&access_token={self.token}&v=5.122")
        return await self.get(url=url)

    async def wall_get(self, owner_id: int):
        url = f"https://api.vk.com/method/wall.get?owner_id={owner_id}&access_token={self.token}&v=5.122"
        return await self.get(url=url)
