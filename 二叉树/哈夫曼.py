class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val < other.val


class my_heap():
    def __init__(self, elist=[]):
        self.val = list[elist]
        if elist:
            self.buildheap()  # 这个地方一直写作了，写成了self.val.buildheap

    def buildheap(self):
        end = len(self.val)
        for i in range(end // 2, -1, -1):
            self.siftdown(self.val[i], i, end)

    def siftdown(self, e, first, end):
        tem = self.val
        i = first
        j = i * 2 + 1
        while j < end:
            if j + 1 < end and tem[j + 1] < tem[j]:
                j += 1
            if e < tem[j]:
                break
            tem[i] = tem[j]
            i = j
            j = j * 2 + 1
        tem[i] = e

    def dequeque(self):
        tem = self.val
        e0 = tem[0]
        e = tem.pop()
        if len(tem) > 0:
            self.siftdown(e, 0, len(tem))
        return e0

    def enqueue(self, e):
        tem = self.val
        tem.append(None)
        last = len(tem) - 1
        i = last
        j = (i - 1) // 2
        while i > 0 and e < tem[j]:
            tem[i] = tem[j]
            i = j
            j = (j - 1) // 2
        tem[i] = e

    def number(self):
        return len(self.val)


def Huffmantree(weights):
    trees = my_heap()
    for w in weights:
        trees.enqueue(Node(w))  # 我这个enqueue是用来是值的 而不是节点啊
    while trees.number() > 1:
        t1 = trees.dequeque()
        t2 = trees.dequeque()
        x = t1.val + t2.val
        trees.enqueue(Node(x, t1, t2))
    return trees.dequeque()


def count_node(t):
    if t is None:
        return 0
    else:
        return 1 + count_node(t.left) + count_node(t.right)


#
# Huffman编码
def huffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes
