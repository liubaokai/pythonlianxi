def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


'''seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]'''


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))


print(Fibonacci_Yield(100))


def fib(n):
    n1 = 1
    n2 = 1
    if n < 1:
        return False
    while n - 2 > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3


print(fib(100))
