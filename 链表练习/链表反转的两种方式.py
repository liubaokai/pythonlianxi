class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def Creat_link_list(n):
    if n <= 0:
        return False
    elif n == 1:
        return Node(1)
    else:
        # cur = Node(1)
        # 这个地方错了 ，因为cur已经变了，应该用一个指针表示
        # for i in range(2, n+1):
        #     cur.next = Node(i)
        #     cur = cur.next
        # return cur
        cur = Node(1)
        tem = cur
        for i in range(2, n + 1):
            tem.next = Node(i)
            tem = tem.next
        return cur


def print_link_list(list):
    cur = list
    while not cur == None:
        print(cur.val)
        cur = cur.next


def reverse2(head):  # 插入逆序
    if head == None or head.next == None:
        return head
    cur = head.next
    head.next = None
    while cur is not None:
        next1 = cur.next
        cur.next = head
        # pre = cur.next# 这个地方不一样呀 应该只向前一个
        head = cur
        cur = next1
    return head


def reverse22(head):  # 就地逆序
    if head == None or head.next == None:  # 都得判断，否则默认head就是ture 直接return了
        return head
    cur = head.next
    head.next = None
    while cur is not None:
        next1 = cur.next
        cur.next = head
        head = cur
        cur = next1
    return head


if __name__ == '__main__':
    a = Creat_link_list(10)
    print_link_list(a)
    b = reverse2(a)
    print_link_list(b)
