import pickle


def read_compressed_file(file_name):
    file = open(file_name, 'rb')
    code_array = pickle.load(file)
    byte_array = pickle.load(file)
    file.close()
    #print(code_array)
    #print(byte_array)
    return code_array,byte_array

def get_bits_chain(byte_array):
    bits_chain =''
    for value in byte_array:
        bits = bin(value)[2:].rjust(8,'0')
        bits_chain += bits
    info_extra_zeros = bits_chain[:8]
    extra_zeros = int(info_extra_zeros,2)
    bits_chain = bits_chain[8:]
    bits_chain=bits_chain[:-1*extra_zeros]
    print (bits_chain)
    return bits_chain

def decompress_text(code_array, bits_chain):
    code = ''
    decompressed_text = ''
    for bit in bits_chain:
        code += bit
        if code in code_array:
            char = code_array[code]
            decompressed_text += char
            code = ''
    print(decompressed_text)
    return decompressed_text


def save_decomppresed_file(file_name, decompressed_text):
    file =open(file_name, 'w', encoding='utf-8')
    file.write(decompressed_text)
    file.close()

def main():
    tablica_kodowa, tablica_bajtów = read_compressed_file('arcio_com')
    łańcuch_bitów = get_bits_chain(tablica_bajtów)
    odkodowany_text = decompress_text(tablica_kodowa, łańcuch_bitów)
    save_decomppresed_file('arcio_decom', odkodowany_text)
main()