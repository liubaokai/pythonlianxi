def findTop3(array):
    if array is None or len(array) < 0:
        return
    r1 = r2 = r3 = -2 ** 31
    i = 0
    while i < len(array):
        if array[i] > r1:
            r3 = r2
            r2 = r1
            r1 = array[i]
        elif array[i] > r2 and array[i] != r1:
            r3 = r2
            r2 = array[i]
        elif array[i] > r3 and array[i] != r2:
            r3 = array[i]
        i += 1
    return r1, r2, r3
