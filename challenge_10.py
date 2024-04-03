# Implement CBC mode

from Crypto.Cipher import AES
from basic_functions import *
from challenge_9 import pkcs_pad_msg
from challenge_2 import xor_bytes

encoding = "utf-8"
blocksize = 16

def ECB_encrypt(msg, key):
    msg = pkcs_pad_msg(msg, blocksize)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)


def ECB_decrypt(emsg, key):
    decipher = AES.new(key, AES.MODE_ECB)
    return decipher.decrypt(emsg)


def CBC_encrypt(msg, key, initial_vector):
    msg = pkcs_pad_msg(msg, blocksize)

    # First block, using the initial vector
    block = xor_bytes(msg[:blocksize], initial_vector)
    cipher_block = ECB_encrypt(block, key)
    ciphertext = cipher_block

    # For each successive block, we use the last cipher block and xor
    # it against the current block.
    for i in range(1, len(msg) // blocksize):
        block = xor_bytes(msg[i * blocksize : (i + 1) * blocksize], cipher_block)
        cipher_block = ECB_encrypt(block, key)
        ciphertext += cipher_block
    return ciphertext


def CBC_decrypt(emsg, key, initial_vector):
    cipher_block = emsg[:blocksize]
    temp_block = ECB_decrypt(cipher_block, key)
    text_block = xor_bytes(temp_block, initial_vector)
    text = text_block
    prev_cipher_block = cipher_block

    for i in range(1, len(emsg) // blocksize):
        cipher_block = emsg[i * blocksize : (i + 1) * blocksize]
        temp_block = ECB_decrypt(cipher_block, key)
        text_block = xor_bytes(temp_block, prev_cipher_block)
        prev_cipher_block = cipher_block
        text += text_block
    return text


if __name__ == "__main__":
    # Before doing the actual problem at hand, let's do some testing.    
    testing_msg = b""" CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.

    In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

    The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

    Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.

    The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c) """
    testing_msg = pkcs_pad_msg(testing_msg, blocksize)
    testing_key = b"HORMONESHORMONES"
    testing_emsg = ECB_encrypt(testing_msg, testing_key)
    testing_dmsg = ECB_decrypt(testing_emsg, testing_key)

    print("Encrypted with ECB:", testing_emsg)
    print("Decrypted with ECB:", testing_dmsg)

    
    initial_vector = b"\xa3" * blocksize

    foo = CBC_encrypt(testing_msg, testing_key, initial_vector)
    bar = CBC_decrypt(foo, testing_key, initial_vector)

    # Okay, now let's solve chalenge 10.
    blocksize = 16
    foo = open("10.txt")
    the_ciphertext = b"".join([x.strip().encode(encoding) for x in
                               foo.readlines()]) 
    foo.close()
    the_ciphertext = decode_base64(the_ciphertext)
    the_key = b"YELLOW SUBMARINE"
    the_iv = b"\x00" * blocksize

    the_plaintext = CBC_decrypt(the_ciphertext, the_key, the_iv)
    print("\n\n")
    print("The original message was:\n\n",
          the_plaintext.decode(encoding))
    print("\n\n")
