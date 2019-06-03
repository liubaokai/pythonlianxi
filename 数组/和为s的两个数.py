def findnumsums(arr, s):
    if not arr:
        return []
    start = 0
    end = len(s) - 1
    while start < end:
        cursum = arr[start] + arr[end]
        if cursum == s:
            return arr[start] + arr[end]
        elif cursum > s:
            end -= 1
        else:
            start += 1
    return []


def sumtos(s):
    a, b = 1, 2
    ret = []
    while a < s / 2 + 1:
        if sum(range(a, b + 1)) == s:
            ret.append(range(a, b + 1))
            a += 1
        elif sum(range(a, b + 1)) < s:
            b += 1
        else:
            a += 1
    return ret
