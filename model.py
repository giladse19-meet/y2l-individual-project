from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Idea(Base):
    __tablename__ = "ideas"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    links = Column(String)
    posx = Column(Integer)
    posy = Column(Integer)