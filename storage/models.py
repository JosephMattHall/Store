import datetime

from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    last_modified = Column(DateTime)

    def __repr__(self):
        return "<File(name='%s', path='%s', last_modified='%s')>" % (
            self.name,
            self.path,
            self.last_modified,
        )