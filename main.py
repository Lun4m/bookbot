import sys


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict[str, int]:
    letter_count = {}
    for char in text:
        c = char.lower()
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    return letter_count


def load_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents


def book_report(file_path: str, word_count: int, char_count: dict[str, int]) -> None:
    print(f"- - - Report for {file_path} - - -")
    print(f"{word_count} words found in the document\n")

    sorted_count = [(char, count) for char, count in char_count.items()]
    sorted_count.sort(key=lambda x: x[1], reverse=True)

    for char, count in sorted_count:
        if char.isalpha():
            print(f"The {char} character was found {count} times")
    print("- - - End report - - -")


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python main.py <path/to/book>")
        exit()

    file_path = sys.argv[1]
    text = load_file(file_path)
    n_words = count_words(text)
    char_count = count_chars(text)
    book_report(file_path, n_words, char_count)


if __name__ == "__main__":
    main()
