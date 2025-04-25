def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(eintrag):
    return eintrag["num"]

def sort_list(liste):
    neulist = []
    for key, value in liste.items():
        if key.isalpha():
            neulist.append({"char": key, "num": value})
    
    neulist.sort(reverse=True, key=sort_on)
    for item in neulist:
        print(f"{item['char']}: {item['num']}")
