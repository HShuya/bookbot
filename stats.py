


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def char_number(text):
    singlechar = list(text)
    counter = {}
    for n in range(0, len(singlechar)):
        symbol = str.lower(singlechar[n])
        if symbol in counter:
            counter[symbol] += 1
        else: 
            counter[symbol] = 1
    return counter

