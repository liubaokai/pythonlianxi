class Node():
    def __init__(self,x):
        self.val = x
        self.next = None

def reverse(li):
    if li == None or li.next == None:
        return li
    new_head = None
    # 没有用指针 那会没想到是指针  但是第一个本来就是个指针
    while li :
        tem = li.next
        li.next = new_head
        new_head = li
        li = tem
    return new_head

def create_ll(arr):
    pre = Node(0)
    tmp = pre  # 相当于指针的概念 说明我没理解之前 现在理解了
    for i in arr:
        tmp.next = Node(i)
        tmp = tmp.next
    return pre.next

def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp=tmp.next


if __name__ == '__main__':
    a = create_ll(range(5))
    # print_ll(a)  # 0 1 2 3 4
    a = reverse(a)
    print_ll(a)  # 4 3 2 1 0

