import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# the secret configuration specific things
from ..Config import Config
#from ..core.logger import logging

#LOGS = logging.getLogger(__name__)

DB_URI = Config.DB_URI

def start() -> scoped_session:
    database_url = DB_URI
    engine = create_engine(database_url)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(e)
except Exception as e:
    print(e)
