# lambda arguments : expression
x = lambda a: a + 10
print(x(5))  # 15

x = lambda a, b: a * b
print(x(5, 6))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)  # lambda a: a * 2
print(mydoubler(11))  # 22


