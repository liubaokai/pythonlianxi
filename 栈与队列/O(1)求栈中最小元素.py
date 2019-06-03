class Mystack():
    def __init__(self):
        self.elemStack = Stack()
        self.minStack = Stack()

    def push(self, data):
        self.elemStack.push(data)
        if self.minStack.empty():
            self.minStack.push(data)
        else:
            if data < self.minStack.peek():
                self.minStack.push(data)

    # 不是每次都弹出，只有弹出等于min【-1】时才弹出
    def pop(self):
        topData = self.elemStack.peek()
        self.elemStack.pop()
        if topData == self.mins():
            self.minStack.pop()
        return topData

    def mins(self):
        if self.minStack.empty():
            return None
        else:
            return self.minStack.peek()


class MyStack(object):
    # 每次都压入
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if self.min and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self):
        if self.stack:
            self.min.pop()
            return self.stack.pop()
        return None

    def min(self):
        return self.min[-1] if self.min else None
