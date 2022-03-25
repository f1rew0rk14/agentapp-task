from typing import Union, Dict, List

from networks_connector.adapters.adapter import Adapter
from networks_connector.adapters.channels.facebook.client import FacebookClient
from networks_connector.adapters.utils.exceptions import (
    UserIdError,
    ClosedProfile,
    UserNotFound
)


class FacebookAdapter(Adapter):
    def __init__(self, token: str, proxy: bool):
        self.client = FacebookClient(token=token, proxy=proxy)

    def __catch_errors(self, error) -> None:
        # По-хорошему надо вкрутить обработку других вариантов, но у апи фейсбука много ограничений,
        # которые не позволяют доставать оттуда всякое без модерации и апрува приложения
        if error:
            if error["code"] == 100:
                raise UserNotFound()

    async def get_profile(self, user: Union[str, int]) -> Dict[str, str]:
        user_info = await self.client.get_user(
            user_id=user,
            fields=["first_name", "last_name", "gender", "birthday", "hometown", "location"]  # Поля возвращаются не все опять же из-за пермитов
        )

        self.__catch_errors(user_info.get("error"))
        return user_info

    async def get_friends(self, user: Union[str, int]) -> List[str]:
        user_friends = await self.client.get_friends(
            user_id=user,
            fields=["first_name", "last_name", "gender", "birthday", "hometown", "location"]
        )
        # Возвращается пустой лист из-за пермитов фейсбука

        self.__catch_errors(user_friends.get("error"))
        return user_friends["data"]

    async def get_wall(self, user: Union[str, int]) -> List[Dict[str, Union[List, Dict, str]]]:
        user_wall = await self.client.get_feed(user_id=user)  # Возвращается пустой лист из-за пермитов фейсбука

        self.__catch_errors(user_wall.get("error"))
        return user_wall["data"]
