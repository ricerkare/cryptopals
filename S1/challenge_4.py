# Q4

Hexes = [i.strip() for i in open("hexes.txt").readlines()]
Fload = []  # list of words by letter
for i in Hexes:
    for case in (65, 97):  # we gonna test all dem chars :D
        for j in range(26):
            Fload.append([chr(case + j), xorz(i, chr(case + j) * len(Hexes))])
guesses = []

"""for i in range(len(Fload)): 
    if checkWords(Fload[i][1])[0] > 0:
        print (i, Fload[i][0])
        print checkWords(Fload[i][1]), Fload[i][1]
        guesses.append([i, Fload[i][1], Fload[i][0]])
for i in guesses:
    print i[1]
    print i[2]
"""

strings_file = open("4.txt")
hexed_lines = strings_file.read.split("\n")
strings_file.close()
