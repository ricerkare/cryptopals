from basic_functions import *
from char_freq import *
from challenge_2 import xor_bytes

# Returns the key to a message that has been xored with a single
# character. Assume argument is of type bytes. The key is found using
# the character frequency score.
def break_single_char_xor(emsg):
    lower = ord("a")  # This is 97, but magic numbers suck.
    upper = ord("A")  # This is 65, but magic numbers suck.
    max_freq = 0
    the_key = ""
    for i in range(26):
        lc_letter = chr(lower + i)
        uc_letter = chr(upper + i)

        # Try lowercase letter.
        new_xor = xor_bytes(emsg, (lc_letter * len(emsg)).encode("ascii"))
        new_freq = freq_score(new_xor.decode("ascii"))
        if new_freq > max_freq:
            max_freq = new_freq
            the_key = lc_letter

        # Try uppercase letter.
        new_xor = xor_bytes(emsg, (uc_letter * len(emsg)).encode("ascii"))
        new_freq = freq_score(new_xor.decode("ascii"))
        if new_freq > max_freq:
            max_freq = new_freq
            the_key = uc_letter
    return the_key


if __name__ == "__main__":
    xored_message = decode_hex(
        b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    )

    # Find the key whose string has the highest frequency score.
    the_key = break_single_char_xor(xored_message).encode("ascii")
    original_message = xor_bytes(xored_message, the_key * len(xored_message))

    print("The key is:", the_key.decode("ascii"))
    print("The message is:", original_message.decode("ascii"))
