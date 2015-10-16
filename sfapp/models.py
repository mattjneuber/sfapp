"""
Simple interactive data table
models.py - model definitions

Author: Matt Neuber
"""

from sqlalchemy import Column, Integer, String, Date
from sfapp.database import Base

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    zip_code = Column(Integer)

    def __init__(self, first_name=None, last_name=None, dob=None, zip_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.zip_code = zip_code

    def __repr__(self):
        return "<Person: %s %s>" % (self.first_name, self.last_name)
