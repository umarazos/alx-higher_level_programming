#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    args = sys.argv
    length = len(args)
    if (length > 2):
        print(f"{length - 1:d} arguments:")
        for i in range(1, length):
            print("{:d}: {:s}".format(i, args[i]))
    elif (length == 1):
        print("{:d} arguments.".format(length - 1))
    else:
        print(f"{length - 1:d} argument:")
        print("{:d}: {:s}".format(length - 1, args[1]))
