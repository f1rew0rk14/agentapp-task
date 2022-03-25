from typing import Union, Dict, List

from networks_connector.adapters.adapter import Adapter
from networks_connector.adapters.channels.vk.client import VkClient
from networks_connector.adapters.utils.exceptions import (
    ClosedProfile,
    UserNotFound
)


class VkAdapter(Adapter):
    def __init__(self, token: str, proxy: bool):
        self.client = VkClient(token=token, proxy=proxy)

    async def __validate_user_id(self, user: Union[str, int]) -> int:
        if isinstance(user, str):
            if user.isdigit():
                return int(user)
            profile = await self.get_profile(user=user)
            if profile.get("is_closed"):
                raise ClosedProfile()
            return int(profile["id"])
        return user

    def __catch_errors(self, error) -> None:
        if error:
            if error["error_code"] == 113:
                raise UserNotFound()

    async def get_profile(self, user: Union[str, int]) -> Dict[str, str]:
        user_info = await self.client.users_get(
            user_id=user,
            fields=["nickname", "domain", "sex", "bdate", "city", "country"]
        )

        self.__catch_errors(user_info.get("error"))
        if not user_info["response"]:
            raise UserNotFound()
        return user_info["response"][0]

    async def get_friends(self, user: Union[str, int]) -> List[Dict[str, str]]:
        user_id = await self.__validate_user_id(user=user)
        user_friends = await self.client.friends_get(
            user_id=user_id,
            fields=["nickname", "domain", "sex", "bdate", "city", "country"]
        )

        self.__catch_errors(user_friends.get("error"))
        return user_friends["response"]["items"]

    async def get_wall(self, user: Union[str, int]) -> List[Dict[str, Union[List, Dict, str]]]:
        user_id = await self.__validate_user_id(user=user)
        user_wall = await self.client.wall_get(owner_id=user_id)

        self.__catch_errors(user_wall.get("error"))
        return user_wall["response"]["items"]
