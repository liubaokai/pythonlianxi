class Node(object):
    # def __init__(self,val): #没准是这个地方出错了
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class link_list():

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        if self._head == None:
            return False
        else:
            return True

    def add(self, val):
        node = Node(val)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            # print(cur.val)
            while cur.next != None:  # 这怎么就死循环了？？因为你没用else啊  问题出现在了又加入了一个新的
                cur = cur.next
            cur.next = node  # 第一次没运行，然后还让这个数node3= node3  形成了双向循环  终于找到原因了

    def print_link_list(self):
        cur = self._head
        while not cur == None:
            print(cur.val, end=',')
            cur = cur.next
        print(end='\n')

    def remove_many(self):

        if self._head == None or self._head.next == None:
            return
        cur = self._head
        while cur.next != None:
            pre = cur
            next = cur.next
            while next != None:
                if cur.val == next.val:
                    pre.next = next.next
                    next = next.next
                else:
                    pre = next
                    next = next.next
            cur = cur.next

    def insert_sort(self):
        if self._head == None:
            return
        cur = self._head.next
        while cur != None:
            p = self._head
            while p != cur and p.val <= cur.val:
                p = p.next
            while p != cur:
                tem = p.val
                p.val = cur.val
                cur.val = tem
                p = p.next
            cur = cur.next


if __name__ == '__main__':
    a = link_list()  # 一开始没有加（）+

    a.add(3)
    a.add(2)
    a.add(4)
    a.add(2)
    a.add(7)
    a.add(4)
    a.add(3)
    a.add(10)
    a.add(9)
    a.add(12)
    a.add(15)
    a.add(16)
    a.add(17)
    a.add(6)
    a.add(5)

    a.print_link_list()
    print(a.is_empty())
    a.remove_many()
    a.insert_sort()
    a.print_link_list()
