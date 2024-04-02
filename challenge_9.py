encoding = "utf-8"


def pkcs_pad_msg(msg, blocksize):
    padlen = blocksize - len(msg) % blocksize
    return msg + padlen * padlen.to_bytes(1, "big")


txt = b"YELLOW SUBMARINE"
print(pkcs_pad_msg(txt, 20))
