import glob
import os
import random
import secrets
import string
from pathlib import Path

from DataBase import Data, insert


def generate_random_files():
    here = os.path.dirname(os.path.realpath(__file__))
    folder = 'example_files'
    path = os.path.join(here, folder)
    if not (Path(path).exists()):
        os.mkdir(os.path.join(here, folder))
    files_count = random.randint(30,300)
    for i in range(files_count):
        end_path = os.path.join(path, str(i)+'.txt')
        size = random.randint(1000, 20000)
        letters_and_digits = string.ascii_letters + string.digits + string.punctuation
        letters = ''.join((random.choice(letters_and_digits) for i in range(size)))
        file = open(end_path , 'w', encoding='utf-8')
        file.write(letters)
        file.close()
        size = os.path.getsize(end_path)
        print(size)
        insert(str(i)+'.txt', size)

def compress_time():
    here = os.path.dirname(os.path.realpath(__file__))
    folder = 'example_files'
    path = os.path.join(here, folder)
    txt_files = glob.glob(path+'/*txt')  #lista



compress_time()



    #generate_random_files()