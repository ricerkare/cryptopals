import base64
import codecs

encoding = "utf-8"


def decode_hex(s):
    return codecs.getdecoder("hex_codec")(s)[0]


def encode_hex(s):
    return codecs.getencoder("hex_codec")(s)[0]


def decode_base64(s):
    return base64.b64decode(s)
    # return codecs.getencoder("base64_codec")(s)[0]


def encode_base64(s):
    return base64.b64encode(s)
    # return codecs.getencoder("base64_codec")(s)[0]

def char_set(s):
    return [c.to_bytes(1, "big") for c in set(s)]

def blockify(x, blocksize):
    return [x[i * blocksize : (i+1) * blocksize] for i in \
            range(int(len(x) // blocksize))]
