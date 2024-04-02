from basic_functions import *
from char_freq import *
from challenge_2 import xor_bytes

encoding = "utf-8"


def single_char_xor(msg, char):
    return xor_bytes(msg, char * len(msg))


def break_single_char_xor(emsg):
    """
    Returns the key to a message that has been xored with a single
    character. Assume argument is of type bytes. The key is found using
    the character frequency score.
    """

    freq_score = -1.0
    the_key = b""

    # We want to find the best frequency score, which will be the
    # minimum, since the frequency score calculates how far the
    # frequency distribution deviates from the expected distribution
    # of letters.
    for i in range(0xFF):
        char = i.to_bytes(1, "big")

        # Try current character.
        new_xor = single_char_xor(emsg, char)
        new_score = freq_diff_score(new_xor)
        if freq_score == -1 or new_score < freq_score:
            freq_score = new_score
            the_key = char

    return the_key, freq_score


if __name__ == "__main__":
    xored_message = decode_hex(
        b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    )

    # Find the key whose string has the highest frequency score.
    the_key = break_single_char_xor(xored_message)[0]
    original_message = xor_bytes(xored_message, the_key * len(xored_message))

    print("The key is:", the_key.decode(encoding))
    print("The message is:", original_message.decode(encoding))
