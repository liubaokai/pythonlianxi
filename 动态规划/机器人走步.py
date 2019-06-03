def f(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return f(x - 1, y) + f(x, y - 1)


x, y = map(int, input().split(','))
print(f(x, y))
