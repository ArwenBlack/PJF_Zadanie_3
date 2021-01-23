import pandas as pd

from DataBase import engine


def get_size_table():
    query = """SELECT* FROM file_size_data"""
    size_table = pd.read_sql(query, engine)
    print(size_table)


get_size_table()