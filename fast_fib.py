#


def fib(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    a = 0
    b = 1
    for i in range(2,x+1):
        c = a + b
        a = b
        b = c
    return b
