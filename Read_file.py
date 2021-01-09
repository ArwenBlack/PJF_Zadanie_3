def read_txt_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    return text

def count_character(text):
    temp_freq = {}
    for char in text:
        if char in temp_freq:
            temp_freq[char] += 1
        else:
            temp_freq[char] = 1
    freq = []
    for char, count in temp_freq.items():
        freq.append((count,char))
    return freq