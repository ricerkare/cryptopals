# Challenge 11
# An ECB/CBC detection oracle

from challenge_9 import pkcs_pad_msg
from challenge_10 import ECB_encrypt, ECB_decrypt, CBC_encrypt,
CBC_decrypt 
from basic_functions import *
import random

blocksize = 16

def gen_AES_key():
    return random.randbytes(blocksize)

def encryption_oracle(msg):
    key = gen_AES_key()
    msg = random.randbytes(random.randint(5, 10)) + msg + \
        random.randbytes(random.randint(5, 10))
    if random.randint(0, 1):
        return ECB_encrypt(msg, key)
    else:
        initial_vector = random.randbytes(blocksize)
        return CBC_encrypt(msg, key, random.randbytes)


def detect_ECB(emsg):
    return blockify(emsg, blocksize) == set(blockify(emsg, blocksize))

