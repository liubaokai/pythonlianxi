class squeue():
    def __init__(self, init_len = 8):
        self.len_ = init_len
        self.elem = [0] * init_len
        self.head_ = 0
        self.num_ = 0

    def is_empty(self):
        return self.num_ == 0

    def peek(self):
        if self.num_ == 0:
            return None
        return self.elem[self.head_]

    def dequeue(self):
        if self.num_ ==0:
            return None
        e = self.elem[self.head_]
        self.head_ = (self.head_+1) % self.len_
        self.num_ -= 1
        return e

    def enqueue(self, e):
        if self.num_ == self.len_:
            self.extend_()
        self.elem[(self.head_ + self.num_) % self.len_] = e
        self.num_ += 1

    def extend_(self):
        old_len = self.len_
        self.len_ *= 2
        new_elem = [0] * self.len_
        for i in range(old_len):
            new_elem[i] = self.elem[(self.head_ + i) % old_len]
        self.elem, self.head_ = new_elem, 0

