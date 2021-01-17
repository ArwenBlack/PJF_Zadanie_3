

def burrows_wheeler_transformation(text):
    length = len(text)
    rotation_table = sorted([text[i:length] + text[0:i] for i in range(length)])
    #print(rotation_table)
    index = rotation_table.index(text)
    text_block = ''.join([q[-1] for q in rotation_table])
    new_text = str(index) + text_block
    return new_text


def burrows_wheeler_restore(text):
    index = int(text[0])
    trans_text = text[1:]
    length = len(trans_text)
    index_table = sorted([(i, x) for i, x in enumerate(trans_text)], key=lambda tup: tup[1])
    #print(index_table)
    table = [None] * length
    for i, y in enumerate(index_table):
        j = y[0]
        table[j] = i

    #print(table)
    vector_i = [index]
    for i in range(1, length):
        vector_i.append(table[vector_i[i - 1]])
    #print(vector_i)
    restored_text_table = [trans_text[i] for i in vector_i]
    restored_text_table.reverse()
    restored_text_s = ''.join([str(elem) for elem in restored_text_table])
    return restored_text_s


