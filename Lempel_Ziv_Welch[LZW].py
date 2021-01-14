from io import StringIO
from struct import pack, unpack


class LZW:
    def __init__(self):
        self.dict_size = 256

    def compress(self, input_file):
        dict_size = 1112064  #ZNAKI UTF-8 - może da się jakoś zmiejszyć
        dictionary = {chr(i): i for i in range(dict_size)}
        string = ''
        compressed = []
        for char in input_file:
            new_string = string + char
            if new_string in dictionary:
                string = new_string
            else:
                compressed.append(dictionary[string])
                dictionary[new_string] = dict_size
                dict_size += 1
                string = char
        if string:
            compressed.append(dictionary[string])
        #print(compressed)
        return compressed

    def read_compressed_file(self, com_file):
        compressed_data = []
        while True:
            read_data = com_file.read(4)
            if len(read_data) != 4:
                break
            (data, ) = unpack('!i', read_data)
            compressed_data.append(data)
        return compressed_data

    def decompress(self, compressed_data):
        dict_size = 1112064
        dictionary = dict((i, chr(i)) for i in range(dict_size))
        decompressed_data = StringIO()
        string = chr(compressed_data.pop(0))
        decompressed_data.write(string)
        for symbol in compressed_data:
            if symbol in dictionary:
                entry = dictionary[symbol]
            elif symbol == dict_size:
                entry = string + string[0]
            else:
                raise ValueError('Bad compressed symbol: %s' % symbol)
            decompressed_data.write(entry)
            dictionary[dict_size] = string + entry[0]
            dict_size += 1
            string = entry
        #print(decompressed_data.getvalue())
        return decompressed_data.getvalue()


def main():
    file = open('arcio.txt', 'r', encoding='utf-8')
    data = file.read()
    file.close()
    lzw = LZW()
    compressed = lzw.compress(data)
    file = open('arcio_lzw_com.txt', 'wb')
    for data in compressed:
        file.write(pack('!i', int(data)))
    file.close()
    file = open('arcio_lzw_com.txt', 'rb')
    compressed = lzw.read_compressed_file(file)
    decompressed = lzw.decompress(compressed)
    file = open('arcio_lzw_decom.txt', 'w', encoding='utf-8')
    file.write(decompressed)
    file.close()


main()
