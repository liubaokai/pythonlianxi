class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def Creat_llist(n):
    if n <= 0:
        return False
    elif n == 1:
        return Node(1)
    else:
        cur = Node(1)
        tem = cur
        for i in range(2, n + 1):
            # tem.next = i  是应该写成Node的 相当于是一个节点
            tem.next = Node(i)
            tem = tem.next
        return cur  # 现在对于指针这个地方比较懵逼  给的是第一个节点的位置，就知道了下一个了 也就是说创建的没有头结点的


def print_lllist(list):
    tem = list
    while not tem == None:
        print(tem.val)
        tem = tem.next


def reverse(list):
    if list == None or list.next == None:
        return list
    cur = list
    pre = None
    while not cur == None:
        tem = cur.next
        cur.next = pre
        pre = cur
        cur = tem
    return pre  # 返回值这个地方有嗲懵逼了


def reverse2(head):
    if head == None or head.next == None:  # 都得判断，否则默认head就是ture 直接return了
        return head
    cur = head.next
    tem = head
    tem.next = None
    while cur is not None:
        next = cur.next
        cur.next = tem
        tem = cur
        cur = next
    return tem  # 终于找到了问题，是返回值出现了问题，如果返回的是cur ，后边并没有链接


def reverse_linkedlist3(head):
    if head == None or head.next == None:  # 边界条件
        return head
    cur = head  # 循环变量1
    next = head.next  # 循环变量2
    tmp = None  # 保存数据的临时变量
    while next:
        tmp = next.next
        next.next = cur
        cur = next
        next = tmp
    head.next = None
    return cur


if __name__ == '__main__':
    llist = Creat_llist(5)
    a = reverse(llist)
    b = reverse2(llist)

    print("this is a ")
    print_lllist(a)
    print("this is b")
    # print_lllist(b)
