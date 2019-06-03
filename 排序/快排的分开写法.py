# coding=utf-8
#
# def partition(array, left, right):
#     tmp = array[left]
#     while left < right:
#         while left < right and array[right] >= tmp:
#             right -= 1
#         array[left] = array[right]
#         while left < right and array[left] <= tmp:
#             left += 1
#         array[right] = array[left]
#     array[left] = tmp
#     return left



def partition(alist, first, last):
    if first > last:
        return

    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        print(alist)
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        print(alist)
    alist[low] = mid_value
    # print(alist)
    return low


def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid - 1)
        quick_sort(array, mid + 1, right)
    return array


# lst = input().split(',')
# print(quick_sort(lst, 0, len(lst) - 1))

if __name__ == '__main__':
    li = [20,15,14,18,21,36,40,10]
    # print(li)
    partition(li,0,len(li)-1)

    # quick_sort(li, 0, len(li) - 1)
    # print(li)
