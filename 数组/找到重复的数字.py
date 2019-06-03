def find_dup(array):
    if None is array:
        return -1
    lens = len(array)
    result = 0
    i = 0
    while i < lens:
        result ^= array[i]
        i += 1
    j = 1
    while j < lens:
        result ^= j
        j += 1

    return  result


'''或者求和'''
