import sys
from os.path import splitext

import numpy as np
from PIL.Image import Image


class LZ_78:
    def __init__(self, dict_limit = None):
        self.dict_limit = dict_limit   #rozmiar słownika

    def compress(self, file_name):
        #print(byte_array)
        file = open(file_name, 'rb')
        text = file.read()
        file.close()
        input_chars = tuple(text)
        #print(input_chars)
        output_chars = (input_chars[0], )
        dict = {tuple(): (0, ), (input_chars[0], ): (1, )}
        i = 1
        i_chars = 1
        dict_size = [2]
        while i_chars < len(input_chars):
            if not input_chars[i:i_chars + 1] in dict:
                #print(dict[input_chars[i:i_chars]])
                prepend = dict[input_chars[i:i_chars]]
                if sum(dict_size) == 1:
                    prepend += tuple([0 for i in range(len(dict_size) - len(prepend) - 1)])
                else:
                    prepend += tuple([0 for i in range(len(dict_size) - len(prepend))])
                output_chars += prepend + (input_chars[i_chars], )
                dict[input_chars[i:i_chars +1]] = tuple(dict_size)
                for i in range(len(dict_size)):
                    dict_size[i] += 1
                    if dict_size[i] != self.dict_limit:
                        break
                    else:
                        dict_size[i] = 0
                        if i == len(dict_size) - 1:
                            dict_size.append(1)
                i = i_chars + 1
            i_chars += 1
            #print(dict)
        if input_chars[i: i_chars] in dict and i != i_chars:
            prepend = tuple(dict[input_chars[i:i_chars]])
            output_chars += prepend + tuple([0 for i in range(len(dict_size) - len(prepend))])
        file = open(splitext(file_name)[0] + '.lz78_com', 'wb')
        file.write(bytes(output_chars))
        file.close()
        return splitext(file_name)[0] + '.lz78_com'


    def decompress(self, file_name):
        file = open(file_name, 'rb')
        text = file.read()
        file.close()
        input_char = tuple(text)
        output_char = (input_char[0], )
        dict = [tuple(), (input_char[0], )]
        i_char = 1
        byte_number = 1
        dict_size = self.dict_limit
        is_char = False
        i = 0
        while i_char < len(input_char):
            if is_char:
                output_char += (input_char[i_char], )
                dict.append(dict[i] + (input_char[i_char], ))
                is_char = False
                i_char += 1
                if len(dict) == dict_size + 1:
                    byte_number += 1
                    dict_size *= self.dict_limit
            else:
                i = 0
                multiplier = 1
                for j in range(byte_number):
                    i += input_char[i_char + j] * multiplier
                    multiplier *= self.dict_limit
                if i >= len(dict):
                    print(i, len(dict))
                    print(bytes(output_char))
                output_char += dict[i]
                i_char += byte_number
                is_char = True
        file = open(splitext(file_name)[0] + '.lz78_dcom', 'wb')
        file.write(bytes(output_char))
        file.close()
        return splitext(file_name)[0] + '.lz78_dcom'


# lz = LZ_78(256)
# lz.compress('pt.txt')