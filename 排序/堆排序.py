def heap_sort(ele):
    def siftdown(ele, e, begin, end ):
        i = begin
        j =i * 2 + 1
        while j < end:
            if j + 1 < end and ele[j+1] < ele[j]:
                j += 1
            if e < ele[j]:
                break
            ele[i] = ele[j]  #j元素最小，上移
            i = j
            j = j * 2 + 1
        ele[i] = e
    end = len(ele)
    for i in range(end//2, -1, -1):
        siftdown(ele, ele[i], i, end)
    '''构建堆'''
    '''相当于储存在原表末尾中'''
    for i in range((end-1), 0, -1):
        e = ele[i]
        ele[i] = ele[0]
        siftdown(ele, e, 0 , i)
