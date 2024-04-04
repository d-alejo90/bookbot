def main():
    file_content = read_file("books/frankenstein.txt")
    words_count = count_words(file_content)
    letters_dict = count_letters(file_content)
    show_report(words_count, letters_dict, "books/frankenstein.txt")


def show_report(words_count, letters_dict, file_path):
    print(f"""
    --- Begin of the report of {file_path}---
    Words count: {words_count}
    Letters count:
    """)
    letters_dict.sort(key=sort_on, reverse=True)
    for letter in letters_dict:
        print(f"""
        The {letter['letter']} character was found {letter['count']} times
        """)


def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters_list = []
    letters_dict = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    for key in letters_dict:
        if key.isalpha():
            letters_list.append({
                "letter": key,
                "count": letters_dict[key]
            })
    return letters_list


def sort_on(dict):
    return dict["count"]


main()
