def maxwindow(num, size):
    if size == len(num):
        return [max[num]]
    if size < 1 or size > len(num):
        return []
    res = []
    for i in range(len(num) - size + 1):
        res.append(max(num[i:i + size]))
    return res
print(maxwindow([1,2,3,4,6,2,3,5],3))