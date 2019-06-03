def sort_str(strr):
    if len(strr) < 2:
        return strr
    else:
        pivot = strr[0]
        less = ''.join([i for i in strr[1:] if i >= 'a' and i <= 'z'])
        greater = ''.join([i for i in strr[1:] if i >= 'A' and i <= 'Z'])
        return less + pivot + greater


def sort_str1(strr):
    if len(strr) < 2:
        return strr
    else:
        pivot = strr[0]
        less = ''.join([i for i in strr[1:] if i <= pivot])
        greater = ''.join([i for i in strr[1:] if i >= pivot])
        return sort_str1(less) + pivot + sort_str1(greater)


strr = 'DCABbcad'
print(sort_str(strr))
