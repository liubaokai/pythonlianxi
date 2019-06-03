class stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈空了")
            return None

    def push(self, item):
        self.items.append(item)


def moveBottomToTop(s):
    if s.empty():
        return
    top1 = s.peek()
    s.pop()
    if not s.empty():
        moveBottomToTop(s)
        top2 = s.peek()
        if top1 > top2:
            s.pop()
            s.push(top1)
            s.push(top2)
            return
    s.push(top1)


def reverse_stack(s):
    if s.empty():
        return
    moveBottomToTop(s)
    top = s.peek()
    s.pop()
    reverse_stack(s)
    s.push(top)


if __name__ == '__main__':
    '''栈是先进后出'''
    s = stack()
    s.push(5)
    s.push(4)
    s.push(6)
    s.push(7)
    s.push(1)
    s.push(0)
    reverse_stack(s)


    while not s.empty():
        print(s.peek(), end=',')
        s.pop()

