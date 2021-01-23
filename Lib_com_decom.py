
import zlib, bz2, gzip, lzma
from os.path import splitext


def zlib_best_com(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    compressed_text = zlib.compress(text, zlib.Z_BEST_COMPRESSION)
    file = open(splitext(file_name)[0] + '.zlib_bcom', 'wb')
    file.write(compressed_text)
    file.close()
    return splitext(file_name)[0] + '.zlib_bcom'

def zlib_best_decom(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    decompressed_text = zlib.decompress(text)
    file = open(splitext(file_name)[0] + '.zlib_decom', 'wb')
    file.write(decompressed_text)
    file.close()
    return splitext(file_name)[0] + '.zlib_decom'

def gzip_com(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    file = gzip.GzipFile(splitext(file_name)[0] + '.gz_com', 'wb')
    file.write(text)
    file.close()
    return splitext(file_name)[0] + '.gz_com'

def gzip_decom(file_name):
    file = gzip.GzipFile(file_name, 'rb')
    text = file.read()
    file.close()
    file = open(splitext(file_name)[0] + '.gz_decom', 'wb')
    file.write(text)
    file.close()
    return splitext(file_name)[0] + '.gz_decom'

def bz2_com(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    compressed_text = bz2.compress(text, 9)
    file = open(splitext(file_name)[0] + '.bz2_com', 'wb')
    file.write(compressed_text)
    file.close()
    return splitext(file_name)[0] + '.bz2_com'

def bz2_decom(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    decompressed_text = bz2.decompress(text)
    file = open(splitext(file_name)[0] + '.bz2_decom', 'wb')
    file.write(decompressed_text)
    file.close()
    return splitext(file_name)[0] + '.bz2_decom'

def lzma_com(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    compressed_text = lzma.compress(text)
    file = open(splitext(file_name)[0] + '.lzma_com', 'wb')
    file.write(compressed_text)
    file.close()
    return splitext(file_name)[0] + '.lzma_com'

def lzma_decom(file_name):
    file = open(file_name, 'rb')
    text = file.read()
    file.close()
    decompressed_text = lzma.decompress(text)
    file = open(splitext(file_name)[0] + '.lzma_decom', 'wb')
    file.write(decompressed_text)
    file.close()
    return splitext(file_name)[0] + '.lzma_decom'



# zlib_best_com('arcio.txt')
# zlib_best_decom('arcio.bcom_zlib')
# gzip_com('arcio.txt')
# gzip_decom('arcio.com_gz')

# bz2_com('arcio.txt')
# bz2_decom('arcio.com_bz2')
#
# lzma_com('arcio.txt')
# lzma_decom('arcio.com_lzma')