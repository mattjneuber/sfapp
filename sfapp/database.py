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
