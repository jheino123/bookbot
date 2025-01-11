def main():
    book_path = "books/frankenstein.txt"
    text = print_book(book_path)
    words = count_words(text)
    chars = count_characters(text)
    report = create_report(chars, words, book_path)

def print_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_list = {}
    for character in text.lower():
        if character not in character_list:
            character_list[character] = 1
        else:
            character_list[character] += 1
    return(dict(sorted(character_list.items())))

def create_report(list, word_count, book):
    print(f"--- Begin report of {book} ---\n")
    for item in list:
        if item.isalpha():
            count = list[item]
            print(f"The {item} character was found {count} times")
    print(f"\n{word_count} words found")
    print("--- End of report ---")
main()