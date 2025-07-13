from stats import count_words, count_letters, letter_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_test(file: str) -> str:
    contents = ""
    with open(file) as book:
        contents = book.read()

    return contents

    
def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    book_path = sys.argv[1]
    book_contents = get_book_test(book_path)
    nr_words = count_words(book_contents)
    print(f"Found {nr_words} total words")
    

    letter_count = count_letters(book_contents)
    letter_sorted_count = letter_list(letter_count)
    print("--------- Character Count -------")

    for character in letter_sorted_count:
        print(f"{character["char"]}: {character["num"]}")
    
if __name__ == "__main__":
    main()
