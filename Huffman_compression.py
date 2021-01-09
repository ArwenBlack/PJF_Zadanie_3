# -*- coding: utf-8 -*-
import copy
import pickle

import Read_file


class HuffNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def create_tree(freq):
    def first_node(elem):
        return elem[0]

    q = copy.deepcopy(freq)
    while len(q) > 1:
        q.sort(key=first_node)
        l, r = q.pop(0), q.pop(0)
        print(l, r)
        node = HuffNode(l, r)
        q.append((l[0] + r[0], node))
    # print (q)
    return q[0]


def walk_tree(node, prefix='', codes={}):
    if isinstance(node[1].left[1], HuffNode):
        walk_tree(node[1].left, prefix + '0', codes)
    else:
        codes[node[1].left[1]] = prefix + '0'
    if isinstance(node[1].right[1], HuffNode):
        walk_tree(node[1].right, prefix + '1', codes)
    else:
        codes[node[1].right[1]] = prefix + '1'
    # print (codes)
    return codes


def invert_codes(codes):
    inverted_codes = {}
    for key, value in codes.items():
        inverted_codes[value] = key
    print(inverted_codes)
    return inverted_codes


def encode_text(codes, text):
    encoded_text = ''
    for char in text:
        encoded_text += codes[char]
    print(encoded_text)
    return encoded_text


def prepare_to_byte_save(encoded_text):
    extra_zeros = 8 - len(encoded_text) % 8
    for i in range(extra_zeros):
        encoded_text += '0'
    info_extra_zeros = '{0:08b}'.format(extra_zeros)
    prepared_encoded_text = info_extra_zeros + encoded_text
    print(prepared_encoded_text)
    return prepared_encoded_text

def save_as_bytearray(prepared_encoded_text):
    b = bytearray()
    for i in range(0, len(prepared_encoded_text), 8):
        byte = prepared_encoded_text[i:i+8]
        b.append(int(byte,2))
    print (b)
    return b

def save_compressed_file(file_name, codes_array, byte_array):  #codes_array - invert_codes
    file = open(file_name, 'wb')
    pickle.dump(codes_array, file)
    pickle.dump(byte_array, file)
    file.close()

def main():
    plik = 'arcio.txt'
    tekst = Read_file.read_txt_file(plik)
    czestosc = Read_file.count_character(tekst)
    korzen = create_tree(czestosc)
    kody = walk_tree(korzen)
    tablica_kodowa = invert_codes(kody)
    zakodowany_tekst = encode_text(kody, tekst)
    zakodowany_uzupełniony = prepare_to_byte_save(zakodowany_tekst)
    tablica_bajtów = save_as_bytearray(zakodowany_uzupełniony)
    save_compressed_file('arcio_com', tablica_kodowa, tablica_bajtów)
main()
