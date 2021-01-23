from dataclasses import dataclass

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query

engine = create_engine('sqlite:///file_data.db', echo=True)
Base = declarative_base()


class Data_size(Base):
    __tablename__ = 'file_size_data'
    file_name = Column(String, primary_key=True)
    o_file_size = Column(Integer)
    zlib_file_size = Column(Integer)
    gzip_file_size = Column(Integer)
    bz2_file_size = Column(Integer)
    lzma_file_size = Column(Integer)
    huff_file_size = Column(Integer)
    shan_file_size = Column(Integer)
    lz78_size = Column(Integer)
    lzw_size = Column(Integer)


class Data_time_com(Base):
    __tablename__ = 'file_com_data'
    file_name = Column(String, primary_key=True)
    zlib_time = Column(Integer)
    gzip_time = Column(Integer)
    bz2_time = Column(Integer)
    lzma_time = Column(Integer)
    huff_time = Column(Integer)
    shan_time = Column(Integer)
    lz78_time = Column(Integer)
    lzw_time = Column(Integer)


class Data_time_decom(Base):
    __tablename__ = 'file_decom_data'
    file_name = Column(String, primary_key=True)
    zlib_time = Column(Integer)
    gzip_time = Column(Integer)
    bz2_time = Column(Integer)
    lzma_time = Column(Integer)
    huff_time = Column(Integer)
    shan_time = Column(Integer)
    lz78_time = Column(Integer)
    lzw_time = Column(Integer)


Base.metadata.create_all(engine)


def insert(name, size):
    Session = sessionmaker(bind=engine)
    session = Session()
    (ret,), = session.query(exists().where(Data_size.file_name == name))
    if ret == 1:
        test = update(Data_size).where(Data_size.file_name == name).values(o_file_size=size)
        session.execute(test)
    else:
        test = Data_size(file_name=name, o_file_size=size)
        session.add(test)

    session.commit()


def insert_size(file, size_zlib, size_gzip, size_bz2, size_lzma, size_h, size_s, size_lz78, size_lzw):
    Session = sessionmaker(bind=engine)
    session = Session()
    param_list = list(locals().values())
    col_list = Data_size.__table__.columns.keys()
    data = {}
    for i in range(1, 9):
        if param_list[i] != None:
            data[col_list[i+1]] = param_list[i]
    size_query = session.query(Data_size).filter_by(file_name=file)
    size_query.update(data)
    session.commit()


def insert_time(e, file, time_zlib, time_gzib, time_bz2, time_lzma, time_huff, time_shan, time_lz78, time_lzw):
    Session = sessionmaker(bind=engine)
    session = Session()
    data = {}
    if e == 1:
        d = Data_time_com
    else:
        d = Data_time_decom
    param_list = list(locals().values())
    col_list = d.__table__.columns.keys()
    (ret,), = session.query(exists().where(d.file_name == file))
    if ret == 1:
        for i in range(2, 10):
            if param_list[i] != None:
                data[col_list[i-1]] = param_list[i]
        time_query = session.query(d).filter_by(file_name= file)
        time_query.update(data)
    else:
        test = d(file_name=file)
        session.add(test)
        for i in range(2, 10):
            if param_list[i] != None:
                data[col_list[i - 1]] = param_list[i]
        time_query = session.query(d).filter_by(file_name=file)
        time_query.update(data)
    session.commit()
