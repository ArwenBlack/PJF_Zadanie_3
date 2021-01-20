import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()

class Data(Base):
    __tablename__= 'file_data'
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    o_file_size = Column(Integer)
    huff_file_size = Column(Integer)
    huff_tr_file_size = Column(Integer)
    shan_file_size = Column(Integer)
    shan_tr_file_size = Column(Integer)
    lz78_size = Column(Integer)
    lzw_size = Column(Integer)

    # c_file_size = Column(Float)
    # c_time = Column(Float)
    # d_time = Column(Float)

    def __repr__(self):
        return "<Data(file_name='%s', o_file_size = '%s')>" % (self.file_name, self.o_file_size)

Base.metadata.create_all(engine)

def insert(name, size):
    Session = sessionmaker(bind = engine)
    session = Session()
    test = Data(file_name = name , o_file_size = size)
    session.add(test)
    session.commit()

# Session = sessionmaker(bind = engine)
# session = Session()
# test = Data(file_name = 'name', o_file_size = 123.4)
# session.add(test)
# session.commit()
