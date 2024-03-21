# Challenge 1
# Convert hex to base64
import base64
import codecs


def decode_hex(s):
    return codecs.getdecoder("hex_codec")(s)[0]


def encode_base64(s):
    return codecs.getencoder("base64_codec")(s)[0]


encoding = "ascii"
hex_bytes = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
plaintext = decode_hex(hex_bytes)
base64_bytes = encode_base64(plaintext)
base64_string = base64_bytes.decode(encoding)

print(base64_string)
