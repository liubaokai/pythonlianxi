def get_num(array):
    if array is None or len(array) < 0:
        return
    a = array[0]
    lens = len(array)
    i = 1
    while i < lens:
        a ^= array[i]
        i += 1
    j = 2
    b = 1
    while j <= lens:
        b ^= j
        j += 1
    return a^b