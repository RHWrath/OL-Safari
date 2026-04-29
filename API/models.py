from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from database import Base


# SQLAlchemy ORM model — maps to the destinations table
class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    description = Column(String, nullable=True)


# Pydantic response schema — controls what the API returns
class DestinationSchema(BaseModel):
    name: str
    lat: float
    lng: float
    description: str | None = None

    class Config:
        from_attributes = True
