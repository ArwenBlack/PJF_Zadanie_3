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


def generate_random_files():
    here = os.path.dirname(os.path.realpath(__file__))
    folder = 'example_files'
    path = os.path.join(here, folder)
    if not (Path(path).exists()):
        os.mkdir(os.path.join(here, folder))
    files_count = random.randint(1,15)
    for i in range(files_count):
        end_path = os.path.join(path, str(i)+'.txt')
        size = random.randint(1000, 10000)
        letters_and_digits = string.ascii_letters + string.digits + string.punctuation
        letters = ''.join((random.choice(letters_and_digits) for i in range(size)))
        file = open(end_path , 'w', encoding='utf-8')
        file.write(letters)
        file.close()
        size = os.path.getsize(end_path)
        name = str(i)+'.txt'
        insert(name, size)
        compress_time(name, end_path)
    decompress_time(path)


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


def decom_pom(path, roz, n, func):
    params = [None for i in range(8)]
    files = glob.glob(path + roz)
    for file in files:
        start_time = time.time()
        if n == 4 : func(file, 'huff')
        elif n == 5: func(file, 'shan')
        else: func(file)
        end_time = time.time()
        time_t =  end_time - start_time
        name = os.path.basename(file)
        params[n] = time_t
        insert_time(0, splitext(name)[0] + '.txt', *params)


def decompress_time(path):
    decom_pom(path, '/*zlib_bcom', 0, zlib_best_decom)
    decom_pom(path, '/*gz_com', 1, gzip_decom)
    decom_pom(path, '/*bz2_com', 2, bz2_decom)
    decom_pom(path, '/*lzma_com', 3, lzma_decom)
    a = Statistic_coding_decompression()
    decom_pom(path, '/*huff_com', 4, a.decompression)
    decom_pom(path, '/*shann_com', 5, a.decompression)
    lz78 = LZ_78(256)
    decom_pom(path, '/*lz78_com', 6, lz78.decompress)
    lzw = LZW()
    decom_pom(path, '/*lzw_com', 7, lzw.decompress)







generate_random_files()
#ompress_time()