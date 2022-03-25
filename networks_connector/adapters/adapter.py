from typing import Dict, List
from abc import ABC, abstractmethod


class Adapter(ABC):

    @abstractmethod
    def get_profile(self, user: str) -> Dict:
        """

        :param user: user id or alias
        :return: a dict of user info from social network
        """

    @abstractmethod
    def get_friends(self, user: str) -> List:
        """

        :param user: user id or alias
        :return: a list of user friends with info from social network
        """

    @abstractmethod
    def get_wall(self, user: str) -> List:
        """

        :param user: user id or alias
        :return: a list of user wall posts from social network
        """