from dataclasses import dataclass

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query

engine1 = create_engine('sqlite:///file_data.db', echo=True)
Base = declarative_base()


class Data_size(Base):
    __tablename__= 'file_size_data'
    file_name = Column(String, primary_key=True)
    o_file_size = Column(Integer)
    huff_file_size = Column(Integer)
    shan_file_size = Column(Integer)
    lz78_size = Column(Integer)
    lzw_size = Column(Integer)

    def __repr__(self):
        return "<Data(file_name='%s', o_file_size = '%s')>" % (self.file_name, self.o_file_size)


class Data_time_com(Base):
    __tablename__ = 'file_com_data'
    file_name = Column(String, primary_key=True)
    huff_com_time= Column(Integer)
    shan_com_time = Column(Integer)
    lz78_com_time = Column(Integer)
    lzw_com_time = Column(Integer)


Base.metadata.create_all(engine1)

def insert(name, size):
    Session = sessionmaker(bind = engine1)
    session = Session()
    (ret,), = session.query(exists().where(Data_size.file_name == name))
    if ret == 1:
        test = update(Data_size).where(Data_size.file_name == name).values(o_file_size=size)
        session.execute(test)
    else:
        test = Data_size(file_name = name , o_file_size = size)
        session.add(test)

    session.commit()


def insert_size(file, size_h, size_s, size_lz78, size_lzw):
    Session = sessionmaker(bind=engine1)
    session = Session()
    test = update(Data_size).where(Data_size.file_name == file).values(huff_file_size = size_h,  shan_file_size  = size_s,  lz78_size = size_lz78,  lzw_size = size_lzw)
    session.execute(test)
    session.commit()


# def insert_size(size_h, size_h_tr, size_s, size_s_tr, size_lz78, size_lzw):
#     Session = sessionmaker(bind=engine1)
#     session = Session()
#     test = Data(huff_file_size= size_h, huff_tr_file_size = size_h_tr, shan_file_size  = size_s,  shan_tr_file_size = size_s_tr, lz78_size = size_lz78,  lzw_size = size_lzw)
#     session.add(test)
#     session.commit()



# Session = sessionmaker(bind = engine)
# session = Session()
# test = Data(file_name = 'name', o_file_size = 123.4)
# session.add(test)
# session.commit()
