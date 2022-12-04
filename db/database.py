from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from servicedb.settings import settings

engine = create_engine(
    settings.database_url,
)

Session = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close

Base = declarative_base()