def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    i = gap

    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    li = [1, 5, 67, 3, 7, 45]
    print(li)
    shell_sort(li)
    print(li)
