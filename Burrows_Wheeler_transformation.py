from functools import cmp_to_key

def suffix_array(text):
    return sorted(range(len(text)), key=cmp_to_key(lambda i, j: 1 if text[i:] >= text[j:] else -1))

def burrows_wheeler_transformation(text , suffix_arr):
    return''.join(text[i-1] for i in suffix_arr)

def burrows_wheeler_restore(bwt):
    table = [''for c in bwt]
    for i in range (len(bwt)):
        table = sorted([c + table[i] for i, c in enumerate(bwt)])
    return table[bwt.index('$')]

def main():
    file = open("pt.txt", 'r', encoding='utf-8')
    text = file.read()
    file.close()
    text = text +'$'
    s = suffix_array(text)
    text_n = burrows_wheeler_transformation(text, s)
    file = open("pt_t.txt", 'w', encoding='utf-8')
    file.write(text_n)
    file.close()
    text_r = burrows_wheeler_restore(text_n)
    file = open("pt_to.txt", 'w', encoding='utf-8')
    file.write(text_r)
    file.close()

main()
