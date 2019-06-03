def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_alist = merge_sort(alist[:mid])
    right_alist = merge_sort(alist[mid:])
    left_cur = right_cur = 0
    result = []
    while left_cur < len(left_alist) and right_cur < len(right_alist):
        if left_alist(left_cur) < right_alist(right_cur):
            result.append(left_alist[left_cur])
            left_cur += 1
        else:
            result.append(right_alist[right_cur])
            right_cur += 1
    result += left_alist[left_cur:]  # 就是有一方走完了 一方没走完 加上
    result += right_alist[right_cur:]
    return result
