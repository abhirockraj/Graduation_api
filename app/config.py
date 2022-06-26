from click import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgres://nxpzkbvfdjmqta:4fcb0a4aff18e26977938ad6bdc84e7be4a7b36b4039d447437a6aa936bf4af8@ec2-52-71-23-11.compute-1.amazonaws.com:5432/d100esmnuvhotb'

engine = create_engine(DATABASE_URL,echo= False)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()