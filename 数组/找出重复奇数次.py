def get2num(array):
    if array is None:
        pass
    result = 0
    cur = 0
    i = 0
    while i < len(array):
        result ^= array[i]
        i += 1
    tem = result
    i = result
    while i & 1 == 0:
        cur += 1
        i = i >> 1
    j = 0
    while j < len(array):
        if ((array[j] >> cur) & 1) == 1:
            result ^= array[j]
        j += 1
    print(result)
    print(result^tem)

array= [3,6,6,5,5,4]
get2num(array)
