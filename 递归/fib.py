def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibb(n):
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f2 + f1
    return f2


if __name__ == '__main__':
    print(fibb(20))
    print(fib(20))
