#!/usr/bin/python3
def checker(tup=()):
    if (len(tup) < 2):
        if (len(tup) == 0):
            zero_tup = (0, 0)
            return (zero_tup)
        else:
            return (tup + (0,))
    elif (len(tup) > 2):
        new_tup = tup[:2]
        return (new_tup)
    else:
        return (tup)


def add_tuple(tuple_a=(), tuple_b=()):
    checker1 = checker(tuple_a)
    checker2 = checker(tuple_b)
    return (checker1[0] + checker2[0], checker1[1] + checker2[1])
