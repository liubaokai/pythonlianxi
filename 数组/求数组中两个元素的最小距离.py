def minDistance(array, num1, num2):
    if array is None or len(array) < 0:
        return
    last_cur1 = last_cur2 = -1
    min_distance = 2 ** 32 - 1
    i = 0
    while i < len(array):
        if array[i] == num1:
            last_cur1 = i
            if last_cur2 >= 0:
                min_distance = min(min_distance, abs(last_cur2 - last_cur1))
        if array[i] == num2:
            last_cur2 = i
            if last_cur2 >= 0:
                min_distance = min(min_distance, abs(last_cur2 - last_cur1))
        i += 1
    return min_distance

