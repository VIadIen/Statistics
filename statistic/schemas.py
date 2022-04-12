import datetime
from typing import Optional
from pydantic import BaseModel


class StatisticPost(BaseModel):
    date: datetime.date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None

    class Config:
        orm_mode = True
