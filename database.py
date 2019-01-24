from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_idea(name, content, links, posx, posy):
    idea_object = Idea(name=name, content=content, links=links, posx=posx, posy=posy)
    session.add(idea_object)
    session.commit()

def get_all_ideas():
    ideas = session.query(Idea).all()
    return ideas

def get_idea_by_id(id):
        idea = session.query(Idea).filter_by(id=id).first()
        return idea

