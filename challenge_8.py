# Challenge 8
# Detect AES in ECB mode

from char_freq import *

foo = open("8.txt")
hex_lines = [s.strip() for s in foo.readlines()]
foo.close()

def check_distribution_avg(msg):
    
    
