#!/usr/bin/python3
"""
file similar to model_state.py named model_city.py
that contains the class definition of a City
"""

from sqlalchemy.sql.schema import ForeignKey
from model_state import State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """City class who inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
