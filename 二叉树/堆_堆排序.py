class PrioQueueError(ValueError):
    pass


class Prio_Queue():
    def __init__(self, elist=[]):
        self.val = list[elist]
        if elist:
            self.buildheap()

    def buildheap(self):
        end = len(self.val)  # 既然是长度，那就是超了 多了一个
        for i in range(end // 2, -1, -1):  # 那么end//2 就是父节点的兄弟节点
            self.siftdown(self.val[i], i, end)

    def is_empty(self):
        return not self.val

    def peak(self):
        if self.is_empty():
            raise PrioQueueError("in peal")
        return self.val[0]

    def enqueue(self, e):
        self.val.append(None)  # 相当于长度变长了  否则赋值的时候会显示超出索引
        self.siftup(e, len(self.val) - 1)

    def siftup(self, e, last):  # last 为最后一个元素的位置 同时队列进行了扩充
        """存入元素"""
        elems = self.val
        i = last  # 这时候elems【i】已经是空值 None了  代表着添加进来的位置
        j = (last - 1) // 2  # 父节点
        while i > 0 and e < elems[j]:  # 如果不符合，说明e比最后一个元素的父大
            elems[i] = elems[j]
            i = j
            j = (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self.val
        e0 = elems[0]
        e = elems.pop()  # 默认从最后一个弹出
        if len(elems) > 0:
            self.siftdown(e, 0, len(elmes))
        return e0

    def siftdown(self, e, begin, end):
        elems = self.val
        i = begin
        j = begin * 2 + 1  # 左孩子 j+1 就是右孩子呗
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:  # 如果右小于左
                j += 1  # 取为最小值j
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i = j
            j = j * 2 + 1
        elems[i] = e
