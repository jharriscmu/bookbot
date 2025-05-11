def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file {filepath} was not found."
    except Exception as e:
        return f"An error occurred: {e}"

from stats import count_words

import stats
import sys
import os

def main():
        
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("argv[1] from CLI:", sys.argv[1])
    absolute_script_dir = os.path.dirname(os.path.abspath(__file__))
    print("Script directory:", absolute_script_dir)
    print("Attempted joined path:", os.path.join(absolute_script_dir, sys.argv[1]))
    
    book_path_from_cli = sys.argv[1]
    book_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), book_path_from_cli)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    try:
        with open(book_path, 'r', encoding='utf-8') as file:
            book_text = file.read()

        word_count = stats.count_words(book_text)
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        char_counts = stats.count_characters(book_text)
        sorted_char_counts = stats.sort_character_counts(char_counts)
            
        for item in sorted_char_counts:
            print(f"{item['char']}: {item['num']}")

        print("============= END ===============")

    except FileNotFoundError:
        print(f"Error: File not found at '{book_path}'. ")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
        main()
        