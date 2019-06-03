def reverseNode(head):
    '''这种是head不存值的'''
    if head is None or head.next is None:
        return head
    cur = head.next
    pre = head
    tem = None
    while cur is not None and cur.next is not None:#为什么把or改为and就没事了？？
        '''应该是到到了最后一位没有next了'''
        tem = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = tem
        pre = cur
        cur = tem
    return head
def myown(head):
    '''这是我自己写的，head是存值的
    奇数个不好解决'''
    if head is None or head.next is None:
        return
    pre = head
    cur = head.next
    head = cur

    while cur is not None and cur.next is not None:
        tem = cur.next
        cur.next = pre
        pre.next = tem.next
        cur = tem.next
        pre = tem
    cur.next = pre
    pre.next = None
    return  head
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def Creat_link_list(n):
    if n <= 0:
        return False
    elif n == 1:
        return Node(1)
    else:
        cur = Node(1)
        tem = cur
        for i in range (2, n+1):
            tem.next = Node(i)
            tem = tem.next
        return cur

def print_link_list(list):
    cur = list
    while not cur == None:
        print(cur.val, end = ',')
        cur = cur.next
    print('')
def reverse2(head):# 插入逆序
    if head == None or head.next == None:
        return head
    cur = head.next
    head.next = None
    while cur is not None:
        next = cur.next
        cur.next = head
        # pre = cur.next# 这个地方不一样呀 应该只向前一个
        head = cur
        cur = next
    return head

if __name__ == '__main__':
    a = Creat_link_list(10)
    print_link_list(a)
    b = myown(a)
    print_link_list(b)

