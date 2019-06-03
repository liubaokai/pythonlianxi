def reverse(array, start, end):
    while start < end:
        tem = array[start]
        array[start] = array[end]
        array[end] = tem
        start += 1
        end -= 1


def shift(array, k):
    if array is None:
        return
    n = len(array)
    k %= n
    reverse(array, 0, n - k - 1)
    reverse(array, n - k, n - 1)
    reverse(array, 0, n - 1)
