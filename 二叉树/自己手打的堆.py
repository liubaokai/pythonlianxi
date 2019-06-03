class priority_queue():
    def __init__(self,elist):
        self.val= list[elist]
        if elist:
            self.buildheap()

    def buildheap(self):
        end = len(self.val)
        for i in range(end//2,-1,-1):
            self.siftdown(self.val[i],i,end)

    def is_empyty(self):
        return not self.val

    def peak(self):
        if self.is_empyty():
            return -1
        return self.val[0]

    def enqueue(self,e):
        self.val.append(None)
        last = len(self.val) - 1
        tem = self.val
        i = last
        j = (last-1) // 2
        while i > 0 and e < tem[j]:
            tem[i] = tem[j]
            i = j
            j = (j-1) // 2
        tem[i] = e    #要严格对其啊

    def dequeue(self):
        if self.is_empyty()
            return  -1
        tem = self.val
        e0 = tem[0]
        e = tem.pop()
        if len(tem) > 0:
            self.siftdown(e, 0,len(tem))
        return e0

    def siftdown(self,e,begin,end):
        tem = self.val
        i = begin
        j = i *2 + 1
        while j < end :
            if j + 1 < end and tem[j + 1] < tem[j]:
                j += 1
            if e < tem[j]:
                break
            tem[i] = tem[j]
            i = j
            j = j *2 + 1
        tem[i] = e

class my_heap():
    def __init__(self,elist):
        self.val= list[elist]
        if elist:
            self.val.buildheap()

    def buildhead(self):
        end =  len(self.val)
        for i in range(end//2, -1 ,-1):
            self.siftdown(self.val[i],i,end)

    def siftdown(self,e,first,end):
        tem = self.val
        i = first
        j =i *2 + 1
        while j < end :
            if j + 1 < end and tem[j+1] < tem[j]:
                j += 1
            if e < tem[j]:
                break
            tem[i] = tem[j]
            i = j
            j = j*2 + 1
        tem[i] = e
    def dequeque(self):
        tem = self.val
        e0 = tem[0]
        e = tem.pop()
        if len(tem) > 0:
            self.siftdown(e,0,len(tem))
        return  e0
    def enqueue(self,e):
        tem = self.val
        tem.append(None)
        last = len(tem) - 1
        i = last
        j = (i - 1)//2
        while i > 0 and e < tem[j]:
            tem[i] = tem[j]
            i = j
            j = (j -1)//2
        tem[i] = e