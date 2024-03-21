import base64
import codecs

encoding = "ascii"


def decode_hex(s):
    return codecs.getdecoder("hex_codec")(s)[0]


def encode_hex(s):
    return codecs.getencoder("hex_codec")(s)[0]


def decode_base64(s):
    return codecs.getencoder("base64_codec")(s)[0]


def encode_base64(s):
    return codecs.getencoder("base64_codec")(s)[0]
