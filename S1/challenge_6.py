# Challenge 6
# Break repeating-key XOR

from basic_functions import *
from challenge_1 import *
from challenge_2 import *
from challenge_3 import *
from challenge_4 import *
from challenge_5 import *


def hamming_dist(s, t):
    dist = 0
    foo = xor_bytes(s, t)
    for x in foo:
        i = 0
        while (x >> i) != 0:
            dist += (x >> i) % 2
            i += 1
    return dist


if __name__ == "__main__":
    file_6 = open("6.txt")
    # base64_emsg = "".join([x.strip() for x in file_6.readlines()]).encode(
    #     encoding
    # )
    base64_emsg = file_6.read().encode(encoding)
    file_6.close()

    emsg = decode_base64(base64_emsg)
    key_avgs = []

    for keysize_guess in range(2, 40):
        avg = 0
        # Let's try comparing ALL the blocks.
        for n in range(len(emsg) // keysize_guess):
            block_0 = emsg[n * keysize_guess : (n + 1) * keysize_guess]
            block_1 = emsg[(n + 1) * keysize_guess : (n + 2) * keysize_guess]
            avg += hamming_dist(block_0, block_1) / keysize_guess
        avg /= len(emsg) // keysize_guess
        key_avgs.append([keysize_guess, avg])

    keysizes = [x[0] for x in sorted(key_avgs, key=lambda x: x[1])[:3]]
    key_guesses = []
    for keysize in keysizes:
        print("Trying keysize", keysize)
        blocks = [
            emsg[n * keysize : (n + 1) * keysize]
            for n in range(int(len(emsg) / keysize))
        ]

        transposed_blocks = [
            b"".join([block[i].to_bytes(1, "big") for block in blocks])
            for i in range(keysize)
        ]

        single_char_keys = [
            break_single_char_xor(block)[0] for block in transposed_blocks
        ]
        key_guess = b"".join(single_char_keys)
        key_guesses.append(key_guess)
        print(key_guess)
