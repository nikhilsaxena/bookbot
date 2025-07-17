import sys
from stats import word_count,char_count,sorted_list

def get_book_text(path):
    file_contents = ''
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        file_content = get_book_text(sys.argv[1])
        num_words = word_count(file_content)
        char_counts = char_count(file_content)
        sorted_dict = sorted_list(char_counts)
        print(f'============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------')
        print(f'Found {num_words} total words\n--------- Character Count -------')
        for item in sorted_dict:
            print(f'{item["char"]}: {item["num"]}')
        print(f'============= END ===============')
    
if __name__ == "__main__":
    main()
