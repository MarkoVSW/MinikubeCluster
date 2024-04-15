from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

ip_address = "10.97.121.187"
port = "5432"

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:password@{ip_address}:{port}/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()