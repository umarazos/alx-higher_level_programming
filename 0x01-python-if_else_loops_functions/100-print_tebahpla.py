#!/usr/bin/python3
i = 1
for letter in range(ord('z'), ord('a') - 1, -1):
    if ((i % 2) == 0):
        letter = letter - 32
    i += 1
    print("{:s}".format(chr(letter)), end="")
