from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://root:@localhost:5432/user_details")
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
Base = declarative_base()
