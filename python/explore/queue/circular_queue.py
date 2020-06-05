class MyCircularQueue:
    def __init__(self, length):
        self.queue = [None] * length
        self.head = 0
        self.tail = 0
        self.length = length
        self.current_size = 0

    def __len__(self):
        return self.current_size

    def Front(self):
        if self.current_size:
            return self.queue[self.head]
        else:
            return -1

    def Rear(self):
        if self.current_size:
            if self.tail - 1 >= 0:
                return self.queue[self.tail - 1]
            else:
                return self.queue[self.length - 1]
        else:
            return -1

    def enQueue(self, value):
        if self.isFull():
            return False

        self.queue[self.tail] = value
        if self.is_end(self.tail):
            self.tail = 0
        else:
            self.tail += 1
        self.current_size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.queue[self.head] = None
        if self.is_end(self.head):
            self.head = 0
        else:
            self.head += 1
        self.current_size -= 1
        return True

    def isEmpty(self):
        if self.current_size == 0:
            return True
        return False

    def isFull(self):
        if self.current_size == self.length:
            return True
        return False

    def is_end(self, position):
        if position + 1 > self.length - 1:
            return True
        return False
