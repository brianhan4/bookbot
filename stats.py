def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def get_char_count(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else: char_dict[lower_char] += 1
    return char_dict

def get_char_list(data):
    new_list = []
    for char, count in data.items():
        new_list.append({"char": char, "num": count})
    return new_list

def sort_on(items):
    return items["num"]

