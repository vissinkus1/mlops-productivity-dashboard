from sqlalchemy import Column, Integer, String, Float, DateTime
from db import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(String, unique=True, index=True)
    name = Column(String)


class Workstation(Base):
    __tablename__ = "workstations"

    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(String, unique=True, index=True)
    name = Column(String)


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    worker_id = Column(String)
    workstation_id = Column(String)
    event_type = Column(String)
    confidence = Column(Float)
    count = Column(Integer, default=0)
