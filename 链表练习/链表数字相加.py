class Node(object):
    # def __init__(self,val): #没准是这个地方出错了
    def __init__(self, val,next = None):
        self.val = val
        self.next = next

class link_list():

    def __init__(self,node = None):
        self._head = node

    def is_empty(self):
        if self._head == None:
            return  False
        else:
            return True

    def add(self,val):
        node = Node(val)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            # print(cur.val)
            while cur.next != None: #这怎么就死循环了？？因为你没用else啊  问题出现在了又加入了一个新的
                cur =cur.next
            cur.next = node  #第一次没运行，然后还让这个数node3= node3  形成了双向循环  终于找到原因了

    # def add(self,val):
    #     node = Node(val)
    #     if self._head == None:
    #         self._head = node
    #     else:
    #         while  self._head.next!= None :
    #                 self._head = self._head.next
    #         self._head.next = node








    def print_link_list(self):
        cur = self._head
        while not cur == None:
            print(cur.val,end='')
            cur = cur.next
        print(end='\n')

    def transport(self):
        cur = self._head
        s = [] #不能用str 否则后边的就不能调用了
        while not cur == None:
            s.append(cur.val)
            cur = cur.next
        num = " "
        print(s)
        print("reverse")
        print(s[::-1])
        print("done")
        for i in s[::-1]:
            num =num + str(i)

        num = int(num)
        return num

    def back(self,val):
        val = str(val)
        list_tem = []
        for i in val:
            list_tem.append(i)
        print(list_tem)

    def reverse_link_list(self):
        if self._head == None or self._head.next == None:
            return
        else:
            # head = self._head
            cur =self._head.next
            self._head.next = None
            # head.next = None
            while  cur!= None:
                tem = cur.next
                cur.next = self._head
                self._head = cur
                cur = tem
            # self._head = head #问题出在了定义一个类函数，就不要用return



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
    def sort_list(self):
        cur = self._head.next
        while cur is not None:
            x = cur.val
            p = self._head
            while p is not cur and p.val <= x: #确定cur指针要插入的位置
                p = p.next
            while p is not cur:  #替换插入的位置元素，后面的元素依次向后替换
                y = p.val  # 保存p的val
                p.val = x  # 将现在p的val赋值为x
                x = y  # 令x变为p的val
                p = p.next  # p的指针向后前进一位
            cur.val = x
            cur = cur.next# 指针向后移动，比较新的插入位置，遍历完
    # def sort_fuck(self):
    #     if self._head == None :
    #         return
    #     cur = self._head.next
    #     while cur != None:
    #         p = self._head
    #         x = cur.val
    #         while p != cur and p.val <= x:
    #             p = p.next
    #         while p != cur:
    #             y = p.val
    #             p.val = x
    #             x = y
    #             p = p.next
    #         cur.val = x #y或者x没区别  操蛋 有区别  区别在于没找到p.val>x的   与前面的x = cur.val对应，否则就成了前面的x
    #         cur = cur.next
    def sort_fuck(self):
        if self._head == None :
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
                '''42421743
12234447'''
             #y或者x没区别  操蛋 有区别  区别在于没找到p.val>x的   与前面的x = cur.val对应，否则就成了前面的x
            cur = cur.next





    def sort_list2(self):#试试双指针的方法
        cur = self._head
        if cur is None or cur.next == None:
            return
        cur = cur.next
        while cur != None:
            p = self._head
            pre = p
            while p !=None and p.val <= cur.val:
                pre = p
                p = p.next
            temp = p.next
            cur.val = p.val








if __name__ == '__main__':
    a = link_list()  #一开始没有加（）+

    a.add(4)
    a.add(2)
    a.add(4)
    a.add(2)
    a.add(1)
    a.add(7)
    a.add(4)
    a.add(3)
    a.print_link_list()
    a.sort_fuck()
    a.print_link_list()
    # b = a.transport()
    # print("this is b")
    # print(b)
    # print("skip")
    a.reverse_link_list()
    # c = a.transport()
    a.print_link_list()
    # a.back(b)
    # a.back(c)

