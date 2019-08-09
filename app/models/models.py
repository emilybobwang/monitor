#-*-coding: utf-8 -*-
'''
1. import model which inherited from parent
2. data type import
3.import data
4.import model
'''
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT,DECIMAL,DATE,TIME,DATETIME
import mysql.connector
from sqlalchemy import create_engine

Base = declarative_base()
metadata =Base.metadata

# memory statistics
class Mem(Base):
    __tablename__= "mem"
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))
    total = Column(DECIMAL(8,2))
    free = Column(DECIMAL(8,2))
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

# swap statistics for linux
class Swap(Base):
    __tablename__= "swap"
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))
    total = Column(DECIMAL(8,2))
    free = Column(DECIMAL(8,2))
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)



# cpu statistics
class Cpu(Base):
    __tablename__= "cpu"
    id = Column(BIGINT,primary_key=True)
    percent = Column(DECIMAL(6,2))
    create_date = Column(DATE)
    create_time = Column(TIME)
    create_dt = Column(DATETIME)

if __name__=="__main__":
    mysql_configs= dict(

        db_host ="127.0.0.1",
        db_name = "monitor",
        db_port =3306,
        db_user="root",
        db_pwd = "root"
    )
    mysql_configs= dict(
        db_host = '127.0.0.1',
        db_name= 'monitor',
        db_port=3306,
        db_user= 'root',
        db_pwd= 'root'
    )
    #link = "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
     #   **mysql_configs

    link = "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
        **mysql_configs
    )



    engine =create_engine(link,encoding='utf-8',echo= True)
    metadata.create_all(engine)
