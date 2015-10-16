"""
Simple interactive data table
database.py - SQLAlchemy ORM functions

Author: Matt Neuber
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#from sfapp import app

#db_path = os.path.join(app.root_path, 'core.db')
engine = create_engine('sqlite:///core.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import sfapp.models
    Base.metadata.create_all(bind=engine)

def prepopulate():
    # populate db
    from sfapp.models import Person
    import datetime
    p = Person(first_name='Bob', last_name='Smith', dob=datetime.date(1985, 9, 21), zip_code=76021)
    db_session.add(p)
    p = Person(first_name='Jill', last_name='McIntyre', dob=datetime.date(1980, 6, 2), zip_code=61761)
    db_session.add(p)
    p = Person(first_name='Meryl', last_name='Fox', dob=datetime.date(1982, 7, 13), zip_code=90078)
    db_session.add(p)
    db_session.commit()
