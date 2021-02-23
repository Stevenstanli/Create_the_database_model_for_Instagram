import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    users
    -
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    usuario = Column(String(250), nullable=False)
    TelePhone = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    id_users = Column(Integer, ForeignKey('users.id'))
    Password = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_post = Column(Integer, ForeignKey('post.id'))
    date = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    post = Column(String(250), nullable=False)

class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    id_post = Column(Integer, ForeignKey('post.id'))
    tag = Column(String(250), nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_post = Column(Integer, ForeignKey('post.id'))
    comment = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram1.png')