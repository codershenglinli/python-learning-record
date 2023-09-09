import sys


def fabonacci(totalnum):
    a, b, c = 0, 0, 1
    while True:
        if (a > totalnum):
            return
        yield c
        b, c = c, b+c
        a += 1


f = fabonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()




