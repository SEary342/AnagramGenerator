def main():
    word_set = open_src_dict("popular.txt")
    exact_order_mode = startup_prompt()
    while True:
        letters = str(
            input("Enter letters to search for or (exit/reset) commands: ").strip()
        ).lower()
        if letters == "exit":
            break
        elif letters == "reset":
            exact_order_mode = startup_prompt()
            continue
        else:
            letters = list(letters)
        letter_combos = get_words(letters, word_set, exact_order_mode)
        print(f"\nFound words:\n{letter_combos}\n")


def startup_prompt():
    while True:
        exact_order_mode = str(
            input("\nExact length and order search mode (include ?'s) Y/(N): ")
        ).lower()
        if exact_order_mode in ["", "n"]:
            exact_order_mode = False
            break
        elif exact_order_mode == "y":
            exact_order_mode = True
            break
        else:
            continue
    return exact_order_mode


def get_words(letters: list, word_set: set, exact_order: bool = False) -> dict:
    max_word_len = len(letters)

    words = {k: [] for k in range(3, max_word_len + 1)}
    for k, v in words.items():
        if exact_order and k != max_word_len:
            continue
        base_list = [x for x in word_set if len(x) == k]

        for item in base_list:
            local_letters = letters.copy()
            letter_list = list(item.lower())
            for i, letter in enumerate(letter_list):
                if exact_order:
                    if letter == local_letters[i] or local_letters[i] == "?":
                        if i == len(letter_list) - 1:
                            words[k].append(item)
                        else:
                            continue
                    else:
                        break
                else:
                    if letter in local_letters:
                        local_letters.remove(letter)
                    elif "?" in local_letters:
                        local_letters.remove("?")
                    else:
                        break
                    if i == len(letter_list) - 1:
                        words[k].append(item)
    words = {k: v for k, v in words.items() if len(v) > 0}
    return words


def open_src_dict(file_name: str) -> set:
    with open(file_name, "r") as words:
        word_set = set(words.read().split())
    return word_set


if __name__ == "__main__":
    main()
