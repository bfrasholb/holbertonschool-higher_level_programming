#!/usr/bin/python3
"""Module for Base and State Class"""

from sqlalchemy import Column, integer, string
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class State(Base):
    id = Column(integer, primarykey=True, autoincrement=True)
    name = Column(string(128), nullable=False)
