def partition(array, first, last, k):
    if first > last:
        return
    mid = array[first]
    low = first
    high = last
    while low < high:
        while low < high and array[high] >= mid:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < mid:
            low += 1
        array[high] = array[low]
    array[low] = mid
    index = low
    if index == k:
        return array[:k]
    elif index > k:
        return partition(array, first, low - 1, k)
    else:
        return partition(array, low + 1, last, k)
arr = [4, 5, 3, 2, 6]
print(partition(arr, 0, len(arr) - 1, 3))
