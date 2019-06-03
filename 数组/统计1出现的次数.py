def count_1(n):
    count = 0
    for i in range(1, n + 1):
        s = str(i)
        count += s.count('1')
    print(count)


count_1(12)
