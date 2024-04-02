from Crypto.Cipher import AES
from basic_functions import *

encoding = "utf-8"


def ECB_decrypt(emsg, key):
    decipher = AES.new(key, AES.MODE_ECB)
    return decipher.decrypt(emsg)


if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    with open("7.txt") as file_7:
        emsg = file_7.read()
    emsg = decode_base64(emsg)
    msg = ECB_decrypt(emsg, key)
    print(msg.decode())
