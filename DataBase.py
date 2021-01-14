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
    file_format = Column(String)
    o_file_size = Column(Float)
    c_file_size = Column(Float)
    c_time = Column(Float)
    d_time = Column(Float)

    def __repr__(self):
        return "<Data(file_name='%s', file_format = '%s')>" % (self.file_name, self.file_format)


Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
test = Data(file_name = 'name', file_format = 'format', o_file_size = 123.4)
session.add(test)
session.commit()
