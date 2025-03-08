import sys
from stats import get_words, char_count, char_sort

if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    path = sys.argv[1]
    #path = "books/frankenstein.txt"
    title = " BOOKBOT "
    wc = " Word Count "
    cc = " Character Count "
    end = " END "
    file = get_book_text(path)
    num_words = get_words(file)
    num_chars = char_count(file)
    sorted = char_sort(num_chars)
    print (title.center(34, '='))
    print (f"Analyzing book found at {path}...")
    print (wc.center(34, '-'))
    print (f"Found {num_words} total words")
    print (cc.center(34, '-'))
    for item in sorted:
        if item['Character'].isalpha():
            print(f"{item['Character']}: {item['Count']}")
    print (end.center(34, '='))
    

main()