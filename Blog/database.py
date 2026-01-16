from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Base = declarative_base()


SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
