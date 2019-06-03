def select_sort(alist):
    for j in range(len(alist) - 1):
        min_index = j
        for i in range(j + 1, len(alist)):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[i], alist[min_index] = alist[min_index], alist[i]
