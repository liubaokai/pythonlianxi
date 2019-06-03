def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True


# 浮点数相等不能直接用==

def power(base, exponent):
    ans = 1
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent > 0:
        for i in range(exponent):
            ans = base * ans
    else:
        for i in range(-exponent):
            ans = base * ans
        ans = 1 / ans
    return ans
