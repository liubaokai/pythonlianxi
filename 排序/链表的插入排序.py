def insert_sort(head):
    '''没问题 亲测可用'''
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
    n = len(alist)  # 从后往前比较
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1  # 是这个地方蒙了 以为执行完if 后 再去之行else 哈哈哈

            else:
                break


class record():
    def __init__(self, key, data):
        self.key = key
        self.data = data


def insert_record(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        while j > 0:
            if alist[j - 1].key > alist[j].key:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                j -= 1
            else:
                break
