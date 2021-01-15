# -*- coding: utf-8 -*-
import copy
import pickle
import Read_file


def save_as_bytearray(prepared_encoded_text):
    b = bytearray()
    for i in range(0, len(prepared_encoded_text), 8):
        byte = prepared_encoded_text[i:i + 8]
        b.append(int(byte, 2))
    return b


def create_tree(freq):
    def first_node(elem):
        return elem[0]
    q = copy.deepcopy(freq)
    while len(q) > 1:
        q.sort(key=first_node)
        l, r = q.pop(0), q.pop(0)
        node = HuffNode(l, r)
        q.append((l[0] + r[0], node))
    return q[0]


def invert_codes(codes):
    inverted_codes = {}
    for key, value in codes.items():
        inverted_codes[value] = key
    return inverted_codes


def prepare_to_byte_save(encoded_text):
    extra_zeros = 8 - len(encoded_text) % 8
    for i in range(extra_zeros):
        encoded_text += '0'
    info_extra_zeros = '{0:08b}'.format(extra_zeros)
    prepared_encoded_text = info_extra_zeros + encoded_text
    return prepared_encoded_text


def encode_text(codes, text):
    encoded_text = ''
    for char in text:
        encoded_text += codes[char]
    return encoded_text


def save_compressed_file(file_name, codes_array, byte_array):  # codes_array - invert_codes
    file = open(file_name, 'wb')
    pickle.dump(codes_array, file)
    pickle.dump(byte_array, file)
    file.close()


class HuffNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk_tree(self, node, prefix='', codes={}):
        if isinstance(node[1].left[1], HuffNode):
            self.walk_tree(node[1].left, prefix + '0', codes)
        else:
            codes[node[1].left[1]] = prefix + '0'
        if isinstance(node[1].right[1], HuffNode):
            self.walk_tree(node[1].right, prefix + '1', codes)
        else:
            codes[node[1].right[1]] = prefix + '1'
        return codes

    def compress(self, file_name):
        text = Read_file.read_txt_file(file_name)
        freq = Read_file.count_character(text)
        node = create_tree(freq)
        codes = self.walk_tree(node)
        codes_table = invert_codes(codes)
        encoded_text = encode_text(codes, text)
        encoded_filled = prepare_to_byte_save(encoded_text)
        byte_table = save_as_bytearray(encoded_filled)
        save_compressed_file('arcio_com.txt', codes_table, byte_table)


def main():
    h = HuffNode()
    h.compress('arcio.txt')


main()
