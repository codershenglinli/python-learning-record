def function():
    length = 100
    a = 0
    b = 1
    i = 0
    for i in range(length):
        print(b)
        a, b = b, a+b
