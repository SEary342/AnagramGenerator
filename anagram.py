def main():
    word_set = open_src_dict("enable1.txt")
    exact_order_mode = startup_prompt()
    letters = ""
    while True:
        if letters == "" or not exact_order_mode:
            letters = available_letters_prompt()
        if letters == "exit":
            break
        elif letters == "reset":
            exact_order_mode = startup_prompt()
            continue
        else:
            letters = list(letters)
        letter_order = []
        if exact_order_mode:
            letter_order = str(
                input("Enter word to search for (?'s for unknown letters): ")
            ).lower()
            if letter_order == "exit":
                break
            elif letter_order == "reset":
                exact_order_mode = startup_prompt()
                continue
            letter_order = list(letter_order)
            if len(letter_order) > len(letters):
                print(
                    "The provided word to search for must not be longer than the"
                    + "available letters"
                )
                continue
        letter_combos = get_words(letters, word_set, exact_order_mode, letter_order)
        print(f"\nFound words:\n{letter_combos}\n")


def startup_prompt():
    while True:
        exact_order_mode = str(
            input("\nExact length and order search mode Y/(N): ")
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


def available_letters_prompt():
    return str(input("Enter letters to search for: ").strip()).lower()


def get_words(
    letters: list, word_set: set, exact_order: bool = False, letter_order: list = []
) -> dict:
    if exact_order:
        max_word_len = len(letter_order)
    else:
        max_word_len = len(letters)

    words = {k: [] for k in range(3, max_word_len + 1)}
    for k, v in words.items():
        if exact_order and k != max_word_len:
            continue
        base_list = [x for x in word_set if len(x) == k]

        for item in base_list:
            local_letters = letters.copy()
            local_order = letter_order.copy()
            letter_list = list(item.lower())
            for i, letter in enumerate(letter_list):
                if exact_order:
                    if letter in local_letters and (
                        letter == local_order[i] or local_order[i] == "?"
                    ):
                        local_letters.remove(letter)
                        if i == len(letter_list) - 1:
                            words[k].append(item)
                        else:
                            continue
                    else:
                        break
                else:
                    if letter in local_letters:
                        local_letters.remove(letter)
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
