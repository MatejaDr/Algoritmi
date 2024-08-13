class Queue():
    def __init__(self):
        self.data = list()
        self.size = 0
    
    def enqueue(self, item):
        self.data.append(item)
        self.size += 1
    
    def is_empty(self):
        return self.size == 0

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            item = self.data.pop(0)
            self.size -= 1

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.data[0]

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size
    
    def is_empty(self):
        return self.count == 0
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def __iter__(self):
        return iter(self.queue[self.front:self.rear])

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.front())
q.dequeue()
q.dequeue()
print(q.front())

cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.peek())
cq.dequeue()
print(cq.peek())
cq.enqueue(4)
cq.enqueue(5)
print(cq.is_full())
try:
    cq.enqueue(6)
except Exception as e:
    print(e)
