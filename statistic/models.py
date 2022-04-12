from sqlalchemy import Column, DATE, INTEGER, FLOAT
from sqlalchemy.orm import column_property
from statistic.database import Base


class Statistic(Base):
    __tablename__ = "data_static"
    date = Column(DATE, primary_key=True, index=True)
    views = Column(INTEGER, nullable=False, default=0)
    clicks = Column(INTEGER, nullable=False, default=0)
    cost = Column(FLOAT, nullable=False, default=0)
    try:
        cpc = column_property(cost / clicks)
    except():
        cpc = 0
    try:
        cpm = column_property(cost/views*1000)
    except():
        cpm = 0

