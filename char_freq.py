import string

encoding = "utf-8"

# The average frequency of each letter of the alphabet, and also the
# space character.
char_freq = {
    b"A": 0.0651738,
    b"B": 0.0124248,
    b"C": 0.0217339,
    b"D": 0.0349835,
    b"E": 0.1041442,
    b"F": 0.0197881,
    b"G": 0.0158610,
    b"H": 0.0492888,
    b"I": 0.0558094,
    b"J": 0.0009033,
    b"K": 0.0050529,
    b"L": 0.0331490,
    b"M": 0.0202124,
    b"N": 0.0564513,
    b"O": 0.0596302,
    b"P": 0.0137645,
    b"Q": 0.0008606,
    b"R": 0.0497563,
    b"S": 0.0515760,
    b"T": 0.0729357,
    b"U": 0.0225134,
    b"V": 0.0082903,
    b"W": 0.0171272,
    b"X": 0.0013692,
    b"Y": 0.0145984,
    b"Z": 0.0007836,
    b" ": 0.1918182,
}

avg_freq = sum([c ** 2 for c in char_freq.values()])

# for i in range(0xFF):
#     if chr(i) not in string.ascii_uppercase + " ":
#         char_freq[i.to_bytes(1, "big")] = 0


def freq_diff_score(txt):
    # Let's only count lowercase letters, thereby assuming the text is
    # mostly lowercase letters.
    char_count = len(txt)
    txt_freq = {
        ch.encode(): txt.count(ch.encode().lower()) / char_count
        for ch in string.ascii_uppercase + " "
    }
    freq_diff = {
        ch.encode(): abs(txt_freq[ch.encode()] - char_freq[ch.encode()])
        for ch in string.ascii_uppercase + " "
    }
    return sum(freq_diff.values())


# txt = b"On Debian and Ubuntu, the words file is provided by the\
# wordlist package, or its provider packages wbritish, wamerican,\
# etc. On Fedora and Arch Linux, the words file is provided by the words\
# package. The words package is sourced from data from the Moby Project,\
# a public domain compilation of words.["

# print(check_freq(txt))
