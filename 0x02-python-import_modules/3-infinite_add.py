#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    args = sys.argv
    length = len(args) - 1
    total_args = 0
    if (length > 0):
        for i in range(1, length + 1):
            total_args += int(args[i])
        print(f"{total_args:d}")
    else:
        print(length)
