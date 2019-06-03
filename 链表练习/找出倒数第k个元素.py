class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class link_list():

    def __init__(self, node=None):
        self.head_ = node

    def add(self, val):
        '''看来不用指针是不行的，不能self.head当指针用
            因为已经将self.head移动了
            对于不希望移动的还是不要移动了
        '''

        node = Node(val)
        if self.head_ == None:
            self.head_ = node
        else:
            cur = self.head_
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def reverse_link_list(self):
        '''这种情况下可以用，因为希望返回的就是一个head的指针改变的，就省去了重新定义头结点的指向了'''
        if self.head_ == None or self.head_.next == None:
            return
        cur = self.head_.next
        self.head_.next = None
        while cur != None:
            tem = cur.next
            cur.next = self.head_
            self.head_ = cur
            cur = tem

    def find_the_k(self, k):
        if k < 1:
            return
        count = 1
        cur = self.head_
        while count != k:
            cur = cur.next
            count += 1
        print(cur.val)

    def find_the_last_k(self, k):
        if self.head_ is None or self.head_ is None:
            return self.head_
        slow = self.head_
        fast = self.head_
        i = 0
        while i < k and fast is not None:
            fast = fast.next
            i += 1
        if i < k:
            return None
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow.val

    def print_link_list(self):
        '''还是不要直接操作头结点 否则整个链表就毁了'''
        cur = self.head_
        while cur != None:
            print(cur.val, end='')
            cur = cur.next
        print('')


if __name__ == '__main__':
    a = link_list()
    a.add(4)
    a.add(5)
    a.add(1)
    a.add(3)
    a.add(6)
    a.add(3)
    a.add(7)
    a.print_link_list()
    print(a.find_the_last_k(3))
    a.reverse_link_list()
    a.print_link_list()
    a.find_the_k(3)
