from basic_functions import *
from challenge_2 import *
from challenge_3 import *

if __name__ == "__main__":
    strings_file = open("4.txt")
    hexed_lines = strings_file.read().split("\n")
    strings_file.close()
    lines = [decode_hex(line) for line in hexed_lines]

    # Key guesses for each line, and also the character frequency of
    # the xored string.
    key_guesses = [break_single_char_xor(lines[i]) for i in range(len(lines))]
    line_guesses = [
        single_char_xor(lines[i], key_guesses[i][0]) for i in range(len(lines))
    ]

    the_key = b""
    max_freq = 0.0
    the_index = 0

    for i in range(len(key_guesses)):
        # if not line_guesses[i].isascii():
        #     pass
        if key_guesses[i][1] > max_freq:
            max_freq = key_guesses[i][1]
            the_key = key_guesses[i][0]
            the_index = i

    print()
    print(
        "The encrypted message is:",
        hexed_lines[the_index],
        "which is the",
        (str(the_index + 1) + "th line"),
    )
    print("The key is:", the_key.decode(encoding))
    print("The original message is:", line_guesses[the_index].decode(encoding))
