import pandas as pd
import plotly as plt
import plotly.express as px
import plotly.graph_objects as go
from typing import List

from DataBase import engine


def get_size_table():
    query = """SELECT* FROM file_size_data"""
    size_table = pd.read_sql(query, engine)
    return size_table


def get_com_time_table():
    query = """SELECT* FROM file_com_data"""
    c_time_table = pd.read_sql(query, engine)
    return c_time_table


def get_decom_time_table():
    query = """SELECT* FROM file_decom_data"""
    dc_time_table = pd.read_sql(query, engine)
    return dc_time_table


table_size = get_size_table()
com_time_table = get_com_time_table()
decom_time_table = get_decom_time_table()


def get_compression_rate():
    size = pd.DataFrame({'zlib': table_size['zlib_file_size'] / table_size['o_file_size'],
                         'gzip': table_size['gzip_file_size'] / table_size['o_file_size'],
                         'bz2': table_size['bz2_file_size'] / table_size['o_file_size'],
                         'lzma': table_size['lzma_file_size'] / table_size['o_file_size'],
                         'huff': table_size['huff_file_size'] / table_size['o_file_size'],
                         'shan': table_size['shan_file_size'] / table_size['o_file_size'],
                         'lz78': table_size['lz78_size'] / table_size['o_file_size'],
                         'lzw': table_size['lzw_size'] / table_size['o_file_size']
                         })
    a_size = size.mean()
    a_size = pd.DataFrame({'methode': a_size.index, 'rate': a_size.values})
    fig = px.histogram(x=a_size['methode'], y=a_size['rate'])
    fig.update_layout(title='Compression rate', xaxis_title='Methode', yaxis_title='Compression rate')
    fig.update_traces(marker_color='rgb(200, 188, 249)')
    return fig


def size_for_size():
    size = table_size.dropna()
    size['bins'] = pd.qcut(size['o_file_size'], q=5, precision=0).astype(str)
    size = size.groupby('bins').mean().reset_index()
    # print(size)
    fig = go.Figure(data=[go.Bar(
        name='Orginal size', x=size['bins'], y=size['o_file_size'], marker_color='rgb(135, 231, 249)'
    ),
        go.Bar(
            name='zlib size', x=size['bins'], y=size['zlib_file_size'], marker_color='rgb(105, 209, 153)'
        ),
        go.Bar(
            name='gzip size', x=size['bins'], y=size['gzip_file_size'], marker_color='rgb(0, 160, 229)'
        ),
        go.Bar(
            name='bz2 size', x=size['bins'], y=size['bz2_file_size'], marker_color='rgb(0, 99, 229)'
        ),
        go.Bar(
            name='lzma size', x=size['bins'], y=size['lzma_file_size'], marker_color='rgb(0, 15, 229)'
        ),
        go.Bar(
            name='huff size', x=size['bins'], y=size['huff_file_size'], marker_color='rgb(106, 0, 229)'
        ),
        go.Bar(
            name='shan size', x=size['bins'], y=size['shan_file_size'], marker_color='rgb(204, 0, 229)'
        ),
        go.Bar(
            name='lz78 size', x=size['bins'], y=size['lz78_size'], marker_color='rgb(255, 144, 242)'
        ),
        go.Bar(
            name='lzw size', x=size['bins'], y=size['lzw_size'], marker_color='rgb(255, 144, 242)'
        ),
    ]
    )
    fig.update_layout(
        title_text="Compiled file size for orginal file size",
        showlegend=True,
    )
    return fig


def o_size_com_time():
    size_time = pd.concat([table_size['o_file_size'], com_time_table], axis=1).dropna().sort_values('o_file_size')
    fig = go.Figure()
    button_list = []
    iter = 0
    for (columnName, columnData) in size_time.iteritems():
        if columnName != 'o_file_size' and columnName != 'file_name':
            params = [False for i in range(16)]
            params[2 * iter] = True
            params[2 * iter + 1] = True
            fig = fig.add_trace(
                go.Scatter(x=size_time['o_file_size'], y=size_time[columnName], mode='lines', name=columnName))
            fig2 = px.scatter(size_time, x='o_file_size', y=columnName, trendline='ols', trendline_color_override='red')
            fig.add_trace(fig2.data[1])
            button_list.append(
                dict(label=columnName, method='update', args=[{"visible": params}, {"title": columnName}]))
            iter += 1
    fig.layout.update(
        updatemenus=[
            go.layout.Updatemenu(
                active=0, direction="down",
                buttons=list(
                    button_list
                )
            )
        ]
    )
    fig.update_layout(
        title_text="Compliation time for orginal size file",
        showlegend=False,
    )
    return fig

def expected_compressed_size(size):
    if size*100 < table_size['o_file_size'].min():
        a = 10
        variation = 10
    else:
        a = 0.1
        variation = 0.1
    min_size = size - variation*size
    max_size = size + variation*size
    exp_size = table_size[table_size.o_file_size >min_size]
    exp_size = exp_size[exp_size.o_file_size < max_size]
    while(exp_size.empty):
        variation += a
        min_size = size - variation * size
        max_size = size + variation * size
        exp_size = table_size[table_size.o_file_size > min_size]
        exp_size = exp_size[exp_size.o_file_size < max_size]
    columns = exp_size[[i for i in list(exp_size.columns) if i not in ['file_name', 'o_file_size']]]
    pom = exp_size['o_file_size']
    for i in range(8):
         exp_size.iloc[:,i+2] = columns.iloc[:,i]/pom
    exp_size = pd.DataFrame({'methode':exp_size.mean().index, 'rate': exp_size.mean().values }).fillna(0)
    exp_size['exp_size']=  exp_size['rate'] * size
    exp_size= exp_size.astype(({'exp_size': int}))
    values = exp_size['exp_size'].to_list()
    return values

def size_rate_for_not_random_data():
    size_nr = table_size.sort_values('o_file_size')
    size_nr['file_name'] = size_nr.file_name.str.split('.').str[0]
    size_nr = size_nr.drop(size_nr[size_nr['file_name'].str.isdigit()].index)
    for columnName, columnData in size_nr.iteritems():
        if columnName != 'file_name' and columnName != 'o_file_size':
            size_nr[columnName] = size_nr[columnName]/size_nr['o_file_size']

    size_nr = size_nr.mean().drop('o_file_size')
    size_nr = pd.DataFrame({'methode': size_nr.index, 'rate': size_nr.values})
    fig = px.histogram(x=size_nr['methode'], y=size_nr['rate'])
    fig.update_layout(title='Compression rate', xaxis_title='Methode', yaxis_title='Compression rate')
    fig.update_traces(marker_color='rgb(123, 188, 249)')
    return fig

def compression_time_file(file_name):
    table = com_time_table.loc[com_time_table['file_name'] == file_name]
    size = table_size.loc[table_size['file_name'] == file_name]
    colums = []
    values = []
    for columnName, columnData in table.iteritems():
        if columnName != 'file_name':
            colums.append(columnName)
            values.append(float(columnData))
    fig = go.Figure(data = [go.Pie(labels= colums, values=values)])
    fig.update_layout(
        title_text="Compression time of file " + file_name + ". Size: " + str(size.iloc[0]['o_file_size']) ,
    )
    return fig

def get_not_rand_names():
    size_nr = table_size.sort_values('o_file_size')
    size_nr = size_nr.drop(size_nr[size_nr.file_name.str.split('.txt').str[0].str.isdigit()].index)
    list = size_nr['file_name'].to_list()
    return list

# get_compression_rate()
# size_for_size()
# o_size_com_time()
#expected_compressed_size(200000)
#size_rate_for_not_random_data()
#compression_time_file('pt.txt')
get_not_rand_names()