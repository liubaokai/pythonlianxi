def isshunzi(num):
    if not num:
        return False
    num.sort()
    nzero = num.count(0)
    if len(set(num[nzero:])) != len(num[nzero:]):
        return False
    if num[-1] - num[nzero] == len(num) - 1 or num[nzero] + nzero>=num[-1]:
        return True
    return False