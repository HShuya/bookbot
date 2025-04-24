from stats import get_num_words
from stats import get_book_text
from stats import char_number
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    counter = char_number(text)
    print(counter)



main()
