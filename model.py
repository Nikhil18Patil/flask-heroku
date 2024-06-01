from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime


# Define the base class
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name=Column(String(128))
    Class=Column(String(128))
    # Storing the embedding as binary data
    
   

# Create an engine that stores data in the local directory's 'attendance_system.db' file.
engine = create_engine('postgres://u8qnpp16lrlokc:pc57f4b6d899960f551ea2daf1d5c56bc154adc2f9aa570cef24a66c40a665579@cat670aihdrkt1.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d8ol98bf7st656')

# Bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# Create a session
session = DBSession()

# Create all tables in the engine (equivalent to "Create Table" statements in raw SQL)
Base.metadata.create_all(engine)
