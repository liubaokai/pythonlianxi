class Test():
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def arraytotree(self, array, start, end):
        '''把有序数组转换为二叉树'''
        root = None
        if end >= start:
            root = bitnode()
            mid = (start + end + 1)//2
            root.data = arr[mid]
            root.lchild = self.arraytotree(array, start, mid - 1)
            root.rchild = self.arraytotree(array, mid + 1, end )
        else:
            root = None
        return root

    def inordertree(self, root):
        '''将二叉树转换为双向链表'''
        if root is None:
            return
        self.inordertree(root.lchild)
        root.lchild = self.pEnd
        if self.pEnd is None:
            self.pHead = root
        else:
            self.pEnd.rchild = root
        self.pEnd = root
        self.inordertree(root.rchild)
