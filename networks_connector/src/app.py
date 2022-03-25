import sys
import logging
from fastapi import FastAPI, HTTPException, status, Depends

from typing import List

from networks_connector.connector import SocialNetworksConnector
from networks_connector.src.models import InfoRequest
from networks_connector.consts import CHANNELS
from networks_connector.adapters.utils.exceptions import (
    InvalidUserId,
    ClosedProfile,
    UserNotFound
)

api = FastAPI()

logger = logging.getLogger("social_networks_connector")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter("[%(asctime)s]\t%(levelname)7s:\t%(message)s", "%Y-%m-%d %H:%M:%S"))
logger.addHandler(console_handler)

connector = SocialNetworksConnector(proxy=True)


async def safe_execute(method, channel, user):
    try:
        return await method(channel, user)
    except InvalidUserId as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )
    except UserNotFound as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc)
        )
    except ClosedProfile as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc)
        )
    except Exception as exc:
        logger.error(exc, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc)
        )


def validate_channel(request: InfoRequest):
    if request.channel in CHANNELS:
        return request
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="No such channel presented"
    )


@api.get("/get_user_info")
async def create_user(channel: str, user: str):
    return await safe_execute(connector.get_user_info, channel, user)


@api.get("/get_user_friends")
async def create_user(channel: str, user: str):
    return await safe_execute(connector.get_user_friends, channel, user)


@api.get("/get_user_wall")
async def create_user(channel: str, user: str):
    return await safe_execute(connector.get_user_wall, channel, user)


