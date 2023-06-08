#!/usr/bin/python3
if (__name__ == '__main__'):
    from calculator_1 import add, sub, div, mul
    import sys
    args = sys.argv
    length = len(args) - 1
    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    opr = args[2]
    b = int(args[3])
    if (opr == '+'):
        result = add(a, b)
    elif (opr == '-'):
        result = sub(a, b)
    elif (opr == '*'):
        result = mul(a, b)
    elif (opr == '/'):
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {opr} {b} = {result}")
