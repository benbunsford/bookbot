from stats import get_num_words, get_num_chars, sort_dict
import sys

def main(book_path):
    sorted = sort_dict(book_path)
    report = f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {get_num_words(book_path)} total words
--------- Character Count -------"""
    print(report)
    print(*sorted, sep="\n")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
main(book_path)
