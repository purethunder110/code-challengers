from sqlalchemy import Column,Text,String,Boolean,DateTime,Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base,relationship
from DBEngine import engine

import uuid

BASE=declarative_base()

class USERDATA(BASE):
    __tablename__="USERDATA"

    id=Column(UUID(as_uuid=True),primary_key=True)#,default=uuid.uuid4)
    username=Column(String(80),unique=True,nullable=False)
    email=Column(String(120),unique=True,nullable=False)
    password=Column(Text)
    verify=Column(Boolean,unique=False,default=False)
    TwoFA=Column(Boolean,unique=False,default=False)

class SESSION(BASE):
    __tablename__="SESSIONDATA"


    id=Column(Integer,primary_key=True,autoincrement=True)
    sessionID=Column(UUID(as_uuid=True),nullable=False)
    usertype=Column(String(15),nullable=False)
    expire=Column(DateTime,nullable=False)
    host=relationship("USERDATA",back_populates="SESSION")

class QUESTIONHISTORY(BASE):
    __tablename__="QUESTIONHISTORY"

    id=Column(Integer,primary_key=True,autoincrement=True)
    question=Column(Text,nullable=True)
    solution=Column(Text,nullable=True)
    sessiontaken=relationship("SESSION",back_populates="QUESTIONHISTORY")


BASE.metadata.create_all(engine)