def maxproductaftercutting(length):
    if length < 2:
        return -1
    if length == 2:
        return 1
    if length == 3:
        return 2
    li = [0, 1, 2, 3]
    for j in range(4, length + 1):
        Max = 0
        for i in range(1, j):
            temp = li[i] * li[j - i]
            if temp > Max:
                Max = temp
    li.append(Max)
    return li[-1]
