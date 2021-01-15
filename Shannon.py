import math
import pickle


import Read_file
from Huffman_Shannon_decompression import *


class Shannon:
    def __init__(self, text, freq_table):
        self.text = text
        self.freq_table = freq_table

    def get_precision(self):
        precision_dict = {}
        self.freq_table.sort(reverse = True)
        print(self.freq_table)
        p_skumulowane = 0
        for object in self.freq_table:
            precision = math.ceil(-math.log2(object[0]))
            precision_dict[object[1]] = (p_skumulowane, precision)
            p_skumulowane += object[0]
        print(precision_dict)
        return precision_dict

    def get_code(self, precision_dict):
        codes_dict = {}
        for object in precision_dict:
            binary = ""
            fraction = precision_dict[object][0]
            k = precision_dict[object][1]
            while (k):
                fraction *=2
                fract_bit = int(fraction)
                if(fract_bit == 1):
                    fraction -= fract_bit
                    binary += '1'
                else:
                    binary +='0'
                k -=1
            codes_dict[object] = binary
        print(codes_dict)
        return codes_dict

    def get_encoded_text(self, codes_dict):
        encoded_text =''
        for char in self.text:
           encoded_text += codes_dict[char]
        print(encoded_text)
        return encoded_text

    def invert_codes(self, codes_dict):
        inverted_codes = {}
        for key, value in codes_dict.items():
            inverted_codes[value] = key
        print(inverted_codes)
        return inverted_codes

    def prepare_to_byte_save(self, encoded_text):
        extra_zeros = 8 - len(encoded_text) % 8
        for i in range(extra_zeros):
            encoded_text += '0'
        info_extra_zeros = '{0:08b}'.format(extra_zeros)
        prepared_encoded_text = info_extra_zeros + encoded_text
        print(prepared_encoded_text)
        return prepared_encoded_text

    def save_as_bytearray(self, prepared_encoded_text):
        b = bytearray()
        for i in range(0, len(prepared_encoded_text), 8):
            byte = prepared_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        print(b)
        return b

    def save_compressed_file(self, file_name, codes_array, byte_array):  # codes_array - invert_codes
        file = open(file_name, 'wb')
        pickle.dump(codes_array, file)
        pickle.dump(byte_array, file)
        file.close()



def main():
    plik = 'arcio.txt'
    text = Read_file.read_txt_file(plik)
    freq_table = Read_file.count_character_freq(text)
    shannon = Shannon(text, freq_table)
    precision_dict = shannon.get_precision()
    codes_dict = shannon.get_code(precision_dict)
    encoded = shannon.get_encoded_text(codes_dict)
    invert_codes_dict = shannon.invert_codes(codes_dict)
    prepered_encoded_text = shannon.prepare_to_byte_save(encoded)
    bytearray = shannon.save_as_bytearray(prepered_encoded_text)
    shannon.save_compressed_file('arcio_s_com.txt', invert_codes_dict, bytearray)
    tablica_kodowa, tablica_bajtów = read_compressed_file('arcio_s_com.txt')
    łańcuch_bitów = get_bits_chain(tablica_bajtów)
    odkodowany_text = decompress_text(tablica_kodowa, łańcuch_bitów)
    save_decomppresed_file('arcio_s_decom.txt', odkodowany_text)
main()