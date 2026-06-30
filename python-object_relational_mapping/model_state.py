#!/usr/bin/python3
"""Module for Base and State Class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeBase


class Base(DeclarativeBase):
    pass


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primarykey=True, autoincrement=True)
    name = Column(String(128), nullable=False)
