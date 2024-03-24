def pkcs_pad_block(msg, blocksize):
    padlen = blocksize - len(msg)
    return msg + padlen * padlen.to_bytes(1, "big")
