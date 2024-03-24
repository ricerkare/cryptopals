from Crypto.Cipher import AES
from basic_functions import *

encoding = "utf-8"

if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    decipher = AES.new(key, AES.MODE_ECB)
    with open("7.txt") as file_7:
        emsg = file_7.read()
    emsg = decode_base64(emsg)
    print(decipher.decrypt(emsg).decode())
