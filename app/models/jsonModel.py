from typing import List
from pydantic import BaseModel


class ResponseModel(BaseModel):
    From: str = None
    To: str = None
    DeliveryStatus: str = None
    Description: str = None
    Location: str = None
    Date: str = None
    Time: str = None
    TimeStamp: int = None