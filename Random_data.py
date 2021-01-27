import glob
import os
import random
import secrets
import string
import time
from pathlib import Path

from All_statistic_coding_decompression import Statistic_coding_decompression
from DataBase import *
from Huffman import HuffNode
from Lempel_Ziv import LZ_78
from Lempel_Ziv_Welch import LZW
from Lib_com_decom import *
from Shannon import Shannon
from random_words import RandomWords

def generate_random_files(files_count, min_size, max_size, progress_callback):
    r = RandomWords()
    here = os.path.dirname(os.path.realpath(__file__))
    folder = 'example_files'
    path = os.path.join(here, folder)
    if not (Path(path).exists()):
        os.mkdir(os.path.join(here, folder))
    for i in range(files_count):
        progress_callback.emit((i+1)*100/files_count)
        end_path = os.path.join(path, str(i)+'.txt')
        size = random.randint(min_size, max_size)
        letters = ''
        for j in range(size):
            word = r.random_word()
            letters += word
            letters += " "
        file = open(end_path , 'w', encoding='utf-8')
        file.write(letters)
        file.close()
        size = os.path.getsize(end_path)
        name = str(i)+'.txt'
        insert(name, size)
        compress_time(name, end_path)
        decompress_time(path, end_path.split('.txt')[0])


def compress_time(name, file):
    params = []
    start_time = time.time()
    file_name = zlib_best_com(file)
    size_zlib = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time-start_time)

    start_time = time.time()
    file_name = gzip_com(file)
    size_gzip = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time-start_time)

    start_time = time.time()
    file_name = bz2_com(file)
    size_bz2 = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time-start_time)

    start_time = time.time()
    file_name = lzma_com(file)
    size_lzma = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time-start_time)

    start_time = time.time()
    h = HuffNode()
    file_name = h.compress(file)
    size_h = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time-start_time)

    start_time = time.time()
    s = Shannon(file)
    file_name = s.compress()
    size_s = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time - start_time)

    start_time = time.time()
    lz_78 = LZ_78(256)
    file_name = lz_78.compress(file)
    size_lz78 = os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time - start_time)

    start_time = time.time()
    lzw = LZW(file)
    file_name = lzw.compress()
    size_lzw= os.path.getsize(file_name)
    end_time = time.time()
    params.append(end_time-start_time)

    insert_size(name, size_zlib,size_gzip,size_bz2, size_lzma, size_h, size_s,  size_lz78, size_lzw)
    insert_time(1, name, *params)  #1 - com, 0 - decom


def decom_pom(path, file, n, func):
    params = [None for i in range(8)]
    start_time = time.time()
    if n == 4 : func(file, 'huff')
    elif n == 5: func(file, 'shan')
    else: func(file)
    end_time = time.time()
    time_t =  end_time - start_time
    name = os.path.basename(file)
    params[n] = time_t
    insert_time(0, splitext(name)[0] + '.txt', *params)


def decompress_time(path, name):
    decom_pom(path, name + '.zlib_bcom', 0, zlib_best_decom)
    decom_pom(path, name +'.gz_com', 1, gzip_decom)
    decom_pom(path, name +'.bz2_com', 2, bz2_decom)
    decom_pom(path, name +'.lzma_com', 3, lzma_decom)
    a = Statistic_coding_decompression()
    decom_pom(path, name +'.huff_com', 4, a.decompression)
    decom_pom(path, name +'.shann_com', 5, a.decompression)
    lz78 = LZ_78()
    decom_pom(path, name +'.lz78_com', 6, lz78.decompress)
    lzw = LZW()
    decom_pom(path, name +'.lzw_com', 7, lzw.decompress)







#generate_random_files(1,10,20)
#ompress_time()