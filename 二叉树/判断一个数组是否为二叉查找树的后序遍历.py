def  is_after(arr, start, end):
    if arr is None:
        return False
    root = arr[end]
    i = start
    while i < end:
        if arr[i] > root :
            break
        i += 1
    j = i
    while j < end:
        if arr[j] < root:
            return False
        j += 1
    left_is_after = True
    right_is_after = True
    if i > start:
        left_is_after = is_after(arr, start , i-1)
    if j < end:
        right_is_after = is_after(arr, i, end)
    return left_is_after and right_is_after
