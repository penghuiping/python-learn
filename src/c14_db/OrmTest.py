# encoding=utf-8

import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("sqlite:///:memory:", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(Integer, primary_key=True)
    name = sqlalchemy.Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "[User(name='%s', fullname='%s', nickname='%s')]" % (self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='Pen', fullname='Jack Pen', nickname='Pen')
session.add(user1)
session.commit()

users = session.query(User).all()

print(users)
