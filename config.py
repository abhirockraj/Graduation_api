from click import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgres://lfdyhtjcioqgzc:2d8acb8e87b0cc54ed811327506370de7d7467b7e3ceecf2a2d27eda76e84c25@ec2-44-197-128-108.compute-1.amazonaws.com:5432/d4j9u52qg04vk5'

engine = create_engine(DATABASE_URL,echo= False)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()