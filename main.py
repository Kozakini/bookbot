from stats import number_of_words, number_of_letters
import sys
def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return content
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(get_book_text(file_path))} words")
    print("--------- Character Count -------")
    print(number_of_letters(get_book_text(file_path)))
    print("============= END ===============")

if __name__ == "__main__":
    main()

