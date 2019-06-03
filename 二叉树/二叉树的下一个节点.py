class Treelinknode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class solution:
    def getnext(self, pNode):
        if not pNode:
            return pNode
        if pNode.right:
            left = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        while pNode.next:
            tem = pNode.next
            if tem.left == pNode:
                return tem
            pNode = tem
        return None
