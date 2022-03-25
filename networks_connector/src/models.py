from typing import Union
from pydantic import BaseModel


class InfoRequest(BaseModel):
    channel: str
    user: Union[str, int]
