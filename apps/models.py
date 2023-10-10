from .database import Base
from sqlalchemy import Column, Integer, String


class Rooms(Base):  # type: ignore
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<Room %r>" % self.name

    def serialize(self):
        return {"id": self.id, "name": self.name}
