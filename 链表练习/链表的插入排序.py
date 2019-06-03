def insert_sort(head):
    '''没问题 亲测可用，用的是书上第一个方法'''
    if head == None:
        return
    cur = head.next
    while cur != None:
        p = head  # 每次都来一次循环啊  从前往后比较
        while p != cur and p.val <= cur.val:
            p = p.next
        while p != cur:  # 这就是p.val大于cur.val的情况了
            tem = p.val  # 相当于整天向后移动
            p.val = cur.val
            cur.val = tem
            p = p.next
        cur = cur.next


def insert_list(alist):
    n = len(alist)  # 从后往前比较 网上找的方法  相当于是个反向冒泡
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break


class record():
    def __init__(self, key, data):
        self.key = key
        self.data = data
