def word_count(data):
    cleaned_data = data.split()
    return len(cleaned_data)

def char_count(data):
    text = data.lower()
    char_counts = {}
    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def new_dict(chars_dict):
    chars = []
    char_key = {}
    for key, value in chars_dict.items():
        char_key["char"]=key
        char_key["num"]=value
        chars.append(char_key)
        char_key={}
    return chars

def sorted_list(char_dict):
    words = new_dict(char_dict)
    words.sort(reverse=True, key=sort_on)
    return words
