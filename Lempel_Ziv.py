from os.path import splitext
from bitarray import bitarray


encodeNum = lambda num: bin(num).replace("0b","")
getCodeBits = lambda code: 1 if code == 1 else (code-1).bit_length()

def get_number(num, n_bits):
    bNum = encodeNum(num)
    while len(bNum) < n_bits:
        bNum = '0' + bNum

    return bNum

class LZ_78:
    def __init__(self, dict_limit = None):
        self.dict_limit = dict_limit   #rozmiar słownika

    def compress(self, file_name):
        file = open(file_name, "rb")
        bits_in = bitarray()
        bits_in.fromfile(file)  #czytanie pliku jako ciag bitow
        file.close()
        dict_codes = {}
        code = 1 # numer znaku w slowniku
        new_symbol = ""
        bits_out = bitarray()   #ciąg wyjściowych bitow
        i = 0
        while i < bits_in.length():
            f = i + 8
            byte = ''
            for a in str(bits_in[i:f]):   #ciąg 8 bitów na string 0 i 1
                if a== '0' or a =='1':
                    byte += a
            new_symbol += byte
            i = f
            if new_symbol not in dict_codes:  # sprawdzenie czy kolejne znaki (ciagi znaków) są w słowniku
                dict_codes[new_symbol] = code
                value = int(dict_codes[new_symbol[0:-8]]) if len(new_symbol) > 8 else 0   #wartość w slowniku dla złożonego symbolu, 0 dla pojedynczego symbolu
                number_bits = getCodeBits(code)  # 0 lub code (zalezy od tego czy symbol pojedyńczy czy złozony)
                number = get_number(value, number_bits)   #uzupełnionie klucza slwonika (przedrostek 0 lub code)
                bits_out.extend(number)  #ciąg bitów wyjściowych
                bits_out.extend(byte)
                code += 1
                new_symbol = ""
        if new_symbol:
            number_bits = getCodeBits(code)
            number = get_number(int(dict_codes[new_symbol]), number_bits)
            bits_out.extend(number)
        print(bits_out)
        compressed_file = open(splitext(file_name)[0] + '.lz78_com', "wb")
        bits_out.tofile(compressed_file)
        file.close()
        compressed_file.close()
        return splitext(file_name)[0] + '.lz78_com'

    def decompress(self, file_name):
        file = open(file_name, "rb")
        bits = bitarray()
        bits.fromfile(file)
        file.close()
        dict_codes = {0: ""}
        code = 1
        symbol  = ""
        decom_text = bitarray()
        i = 0
        while i < bits.length():
            number_bits = getCodeBits(code)
            f = i + number_bits
            if f > bits.length():
                break
            b = ''
            for a in str(bits[i:f]):
                if a == '0' or a == '1':
                    b += a
            number_code = int(b, 2)
            if f + 8 > bits.length():
                break
            i = f + 8
            dict_codes[code] = dict_codes[number_code] + (bits[f:i]).to01()
            decom_text.extend(dict_codes[code])
            code += 1
        if i < bits.length():
            number_bits = getCodeBits(code)
            b = ''
            for a in str(bits[i:(i + number_bits)]):
                if a == '0' or a == '1':
                    b+= a
            number_code = int(b, 2)
            decom_text.extend(dict_codes[number_code])
        decom_file  = open(splitext(file_name)[0] + '.lz78_dcom', "wb")
        decom_text.tofile(decom_file )
        decom_file .close()
        return splitext(file_name)[0] + '.lz78_dcom'

#
# lz = LZ_78(256)
# lz.compress('arcio.txt')
# lz.decompress('arcio.lz78_com')