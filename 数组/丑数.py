def getugly(index):
    if index <= 0:
        return 0
    index2, index3, index5 = 0, 0, 0
    res = [1]
    while len(res) < index:
        tem = min(res[index2] * 2, res[index3] * 3, res[index5] * 5)
        if not tem in res:
            res.append(tem)
        if tem % 2 == 0:
            index2 += 1
        if tem % 3 == 0:
            index3 += 1
        if tem % 5 == 0:
            index5 += 1
    return res[-1]


print(getugly(10))