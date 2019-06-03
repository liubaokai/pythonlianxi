def quick(alist, first, last):
    if first > last:  # 这个要在最前面写,否则会出现mid超出索引值的情况
        return
    #  迷糊的地方是会不会缺元素，结果是通过mid这个值已经保存了 对 就是这个 还在想12、和16行这个地方会不会导致元素被覆盖没有啦，
    # 但是通过分析，mid保存了

    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # 事实发现 少了这个就是不行  因为如果没有low < high 的判断，那么这个while就会一直循环下去 并不是这么回事，是指针会走过
        # 两种情况都是，并不是上面有等号才会走过，下面的也会走过，只有小于mid，就会向下走一个
        # 接下来是大于号这最后一个问题,那遇到了相等了就不动了 最后指针不重合
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick(alist, first, low - 1)
    quick(alist, low + 1, last)


if __name__ == '__main__':
    li = [12, 15, 15, 4561, 3251, 35, 16854, 1864, 861325, 45641, 6851, 61231, 3541, 561, 351]
    print(li)
    quick(li, 0, len(li) - 1)
    print(li)
