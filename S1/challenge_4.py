# # Q4

# Hexes = [i.strip() for i in open("hexes.txt").readlines()]
# Fload = []  # list of words by letter
# for i in Hexes:
#     for case in (65, 97):  # we gonna test all dem chars :D
#         for j in range(26):
#             Fload.append([chr(case + j), xorz(i, chr(case + j) * len(Hexes))])
# guesses = []

# """for i in range(len(Fload)):
#     if checkWords(Fload[i][1])[0] > 0:
#         print (i, Fload[i][0])
#         print checkWords(Fload[i][1]), Fload[i][1]
#         guesses.append([i, Fload[i][1], Fload[i][0]])
# for i in guesses:
#     print i[1]
#     print i[2]
# """

from basic_functions import *
from challenge_2 import xor_bytes
from challenge_3 import break_single_char_xor

if __name__ == "__main__":
    strings_file = open("4.txt")
    lines = strings_file.read().split("\n")
    strings_file.close()
    # lines = [decode_hex(line) for line in hexed_lines]
    lines = [x.encode(encoding) for x in lines]

    # Key guesses for each line, and also the character frequency of
    # the xored string.
    key_guesses = [break_single_char_xor(lines[i]) for i in range(len(lines))]
    line_guesses = [
        xor_bytes(key_guesses[i][0] * len(lines[i]), lines[i])
        for i in range(len(lines))
    ]

    the_key = b""
    max_freq = 0
    the_index = 0

    for i in range(len(key_guesses)):
        if key_guesses[i][1] > max_freq:
            max_freq = key_guesses[i][1]
            the_key = key_guesses[i][0]
            the_index = i

    print(line_guesses[the_index])
