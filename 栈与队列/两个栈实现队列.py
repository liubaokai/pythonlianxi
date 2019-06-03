class Mystack():
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.empty():
            while not self.A.empty():
                self.B.push(self.A.peek())
                self.A.pop()
        first = self.B.peek()
        self.B.pop()
        return first
