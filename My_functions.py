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
    size = pd.DataFrame({'zlib': table_size['zlib_file_size']/table_size['o_file_size'], 'gzip': table_size['gzip_file_size']/table_size['o_file_size'],
                         'bz2': table_size['bz2_file_size']/table_size['o_file_size'], 'lzma': table_size['lzma_file_size']/table_size['o_file_size'],
                         'huff': table_size['huff_file_size']/table_size['o_file_size'], 'shan': table_size['shan_file_size']/table_size['o_file_size'],
                         'lz78': table_size['lz78_size']/table_size['o_file_size'], 'lzw': table_size['lzw_size']/table_size['o_file_size']
                         })
    a_size = size.mean()
    a_size = pd.DataFrame({'methode':a_size.index, 'rate':a_size.values})
    fig = px.histogram(x= a_size['methode'], y = a_size['rate'])
    fig.update_layout(title = 'Compression rate', xaxis_title = 'Methode', yaxis_title = 'Compression rate')
    fig.update_traces(marker_color='rgb(200, 188, 249)')
    return fig


def size_for_size():
    size = table_size.dropna()
    size['bins'] = pd.qcut(size['o_file_size'], q=5, precision=0).astype(str)
    size = size.groupby('bins').mean().reset_index()
    #print(size)
    fig = go.Figure(data = [go.Bar(
        name= 'Orginal size', x = size['bins'], y = size['o_file_size'], marker_color='rgb(135, 231, 249)'
    ),
    go.Bar(
        name = 'zlib size', x = size['bins'], y = size['zlib_file_size'], marker_color='rgb(105, 209, 153)'
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
    size_time = pd.concat([table_size['o_file_size'], com_time_table], axis =1).dropna().sort_values('o_file_size')
    fig = go.Figure()
    button_list = []
    iter =0
    for (columnName, columnData) in size_time.iteritems():
        if columnName != 'o_file_size' and columnName != 'file_name':
            params = [False for i in range(16)]
            params[2*iter] = True
            params[2*iter +1 ] = True
            fig = fig.add_trace(go.Scatter(x= size_time['o_file_size'], y = size_time[columnName], mode = 'lines', name = columnName))
            fig2 = px.scatter(size_time, x = 'o_file_size', y = columnName, trendline='ols', trendline_color_override='red')
            fig.add_trace(fig2.data[1])
            button_list.append(dict(label = columnName, method = 'update', args = [{"visible": params}, {"title": columnName}]))
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




# get_compression_rate()
#size_for_size()
# o_size_com_time()