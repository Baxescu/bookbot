def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_book_text(path):
    with open(path) as f:
        return f.read()


def num_words(text):
    word_list = text.split()
    return len(word_list)


def char_count(text):
    dictionar = {}
    for c in text.lower():
        if c not in dictionar:
            dictionar[c] = 1
        else:
            dictionar[c] += 1
    return dictionar


def sort_on(items):
    return items["num"]


def sort_dict(items):
    return item.sort(reverse = True, key=sort_on)

def main(path):
    text = get_book_text(path)

    count = num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    chars = char_count(text)
    for char in chars:
        if char.isalnum():
            print(f"{char}: {chars[char]}")
            print()

