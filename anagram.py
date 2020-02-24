def main():
    word_set = open_src_dict("popular.txt")

    while True:
        letters = str(input("Enter letters to search for: ").strip()).lower()
        if letters == "exit":
            break
        else:
            letters = sorted(letters)
        letter_combos = get_words(letters, word_set)
        print(letter_combos)


def get_words(letters: list, word_set: set) -> dict:
    max_word_len = len(letters)

    words = {k: [] for k in range(3, max_word_len + 1)}
    for k, v in words.items():
        base_list = [x for x in word_set if len(x) == k]

        item_list = []
        for item in base_list:
            local_letters = letters.copy()
            letter_list = list(item.lower())
            for i, letter in enumerate(letter_list):
                if letter in local_letters:
                    local_letters.remove(letter)
                elif "?" in local_letters:
                    local_letters.remove("?")
                else:
                    break
                if i == len(letter_list) - 1:
                    words[k].append(item)

    return words


def open_src_dict(file_name: str) -> set:
    with open(file_name, "r") as words:
        word_set = set(words.read().split())
    return word_set


if __name__ == "__main__":
    main()
