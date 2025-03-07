from stats import get_words, char_count, char_sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    path = "books/frankenstein.txt"
    title = " BOOKBOT "
    wc = " Word Count "
    cc = " Character Count "
    file = get_book_text(path)
    num_words = get_words(file)
    num_chars = char_count(file)
    sorted = char_sort(num_chars)
    print (title.center(34, '='))
    print (f"Analyzing book found at {path}...")
    print (wc.center(34, '-'))
    print (f"Found {num_words} total words")
    print (cc.center(34, '-'))
    print (sorted)
    

main()