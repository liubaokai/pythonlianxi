def num1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n - 1
    return ret


print(num1(14))
print(bin(14))
print((14).bit_length())
print(bin(14).count('1'))