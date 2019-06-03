def getmin(arr, low, high):
    if high < low:
        return arr[0]
    if high == low:
        return arr[low]
    mid = (low + high) / 2
    if arr[mid] < arr[mid - 1]:
        return arr[mid]
    elif arr[mid + 1] < arr[mid]:
        return arr[mid + 1]
    elif arr[high] > arr[mid]:
        return getmin(arr, low, mid - 1)
    elif arr[low] < arr[mid]:
        return getmin(arr, mid + 1, high)
    else:  # 考虑相等的情况，这时候无法区分在最小值在左半部分还是右半部分
        return min(getmin(arr, low, mid - 1), getmin(arr, mid + 1, high))
