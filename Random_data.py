import glob
import os
import random
import secrets
import string
from pathlib import Path

from DataBase import *
from Huffman import HuffNode
from Lempel_Ziv import LZ_78
from Lempel_Ziv_Welch import LZW
from Shannon import Shannon


def generate_random_files():
    here = os.path.dirname(os.path.realpath(__file__))
    folder = 'example_files'
    path = os.path.join(here, folder)
    if not (Path(path).exists()):
        os.mkdir(os.path.join(here, folder))
    files_count = random.randint(1,5)
    for i in range(files_count):
        end_path = os.path.join(path, str(i)+'.txt')
        size = random.randint(10000, 30000)
        letters_and_digits = string.ascii_letters + string.digits + string.punctuation
        letters = ''.join((random.choice(letters_and_digits) for i in range(size)))
        file = open(end_path , 'w', encoding='utf-8')
        file.write(letters)
        file.close()
        size = os.path.getsize(end_path)
        name = str(i)+'.txt'
        insert(name, size)
        compress_size(name, end_path)


def compress_size(name, file):
    h = HuffNode()
    file_name = h.compress(file)
    size_h = os.path.getsize(file_name)

    s = Shannon(file)
    file_name = s.compress()
    size_s = os.path.getsize(file_name)

    lz_78 = LZ_78(256)
    file_name = lz_78.compress(file)
    size_lz78 = os.path.getsize(file_name)

    lzw = LZW(file)
    file_name = lzw.compress()
    size_lzw= os.path.getsize(file_name)

    insert_size(name, size_h, size_s,  size_lz78, size_lzw)










generate_random_files()
#ompress_time()