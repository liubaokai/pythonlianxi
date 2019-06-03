def Add(num1, num2):
    # write code here
    nsum = 0
    carrry = 0
    nsum = num1 ^ num2
    carry = (num1 & num2) << 1
    return nsum + carry


# 不能使用加号大哥！！！
def newadd(num1, num2):
    while (num2):
        tem = num1 ^ num2
        num2 = (num1 & num2) << 1
        num1 = tem
    return num1


def newadd1(num1, num2):
    while num2:
        sum = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = sum
        num2 = carry
    return num1


print(Add(5, 7))
print(newadd(5, 7))
print(newadd1(5, 7))
