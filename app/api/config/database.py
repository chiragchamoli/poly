from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.api.config.base import DATABASE_URL

SQLALCHEMY_DATABASE_URL = DATABASE_URL

# TX

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overflow=0,
    pool_pre_ping=True,
    pool_recycle=3600
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Session:
    """Get a database session.

       This function will open a database session and yield it to the caller. The caller
       is responsible for closing the session when they are done with it. If an exception
       is raised, the session will be rolled back.

       Returns:
           A database session.
    """
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()
