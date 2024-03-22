from challenge_2 import *
from challenge_3 import *
from challenge_4 import *
from basic_functions import *


def repeating_key_xor(msg, key):
    emsg = b""
    for i in range(len(msg)):
        emsg += xor_bytes(
            msg[i].to_bytes(1, "big"), key[i % len(key)].to_bytes(1, "big")
        )
    return emsg


if __name__ == "__main__":
    string = b"Burning 'em, if you ain't quick and nimble\nI go crazy \
when I hear a cymbal"

    emsg = repeating_key_xor(string, b"ICE")
    print(encode_hex(emsg).decode(encoding))
