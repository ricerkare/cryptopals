# Challenge 8
# Detect AES in ECB mode

from char_freq import *
from basic_functions import *

def detect_AES_ECB(emsg):
    """
    We are going to see if any block of ciphertext is identical to
    another block of the same length in the same text. If we find
    one such block, assume that it is the ciphertext that has been
    ECB encrypted.
    """
    blocksize = 128 / 8
    block_list = blockify(emsg, blocksize)

    while not found:
        for i in range(len(block_list)):
            test_block_0 = block_list[i]
            for j in range(i + 1, len(block_list)):
                test_block_1 = block_list[j]
                if test_block_0 == test_block_1:
                    return True
    return False
                    

if __name__ == "__main__":
    blocksize = 128 / 8

    foo = open("8.txt")
    hex_lines = [s.strip() for s in foo.readlines()]
    foo.close()
    lines = [decode_hex(hl) for hl in hex_lines]
    index = 0

    for ind in range(len(lines)):
        if detect_AES_ECB(lines[ind]):
            index = ind
    
    print("Index:", index)
    print("Line:", lines[index])
                            
                             
# def check_distribution_avg(msg):
#     expected_sum = sum([c ** 2 for c in english_char_freq.values()])
#     this_sum = 0
#     for freq in freq_dict(msg).values():
#         this_sum += freq ** 2

#     return
