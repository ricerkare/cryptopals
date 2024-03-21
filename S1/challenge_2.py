# Challenge 2
# Fixed XOR
# Write a function that takes two equal-length buffers and produces
# their XOR combination.

import base64
from basic_functions import *

encoding = "ascii"


# Assume x and y are the same length.
def xor_bytes(x, y):
    return bytes([i ^ j for i, j in zip(x, y)])


if __name__ == "__main__":
    B = decode_hex("1c0111001f010100061a024b53535009181c")
    C = decode_hex("686974207468652062756c6c277320657965")

    foo = xor_bytes(B, C)
    foo = encode_hex(foo)
    combination = foo.decode(encoding)

    print(combination)
