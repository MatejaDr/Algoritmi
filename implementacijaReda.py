class LimitedArrayQueue:

    def __init__(self, capacity):
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = -1

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size += 1
        return answer
    
    def enqueue(self, e):
        if self.is_full():
            raise Exception("Queue is full")
        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def is_full(self):
        return self._size == self._capacity
    
    def rotate(self, n):
        if self.is_empty():
            return 
        n = n %self._size
        if n == 0:
            return
        new_data = [None] * self._capacity
        for i in range(n):
            new_data[i] = self._data[(self._front + self._size - n + i) % self._capacity]

        for i in range(self._size - n):
            new_data[n + i] = self._data[(self._front + i) % self._capacity]

        self._data = new_data
        self._front = 0
        self._rear = self._size - 1

    def __str__(self):
        return f"Queue: {self._data}, front: {self._front}, rear: {self._rear}, size: {self._size}"

class ArrayQueue:
    def __init__(self):
        self._data = [None] * 10
        self._size = 0
        self._front = 0
        self._rear = -1

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
    
    def rotate(self, n):
        if self.is_empty():
            return 
        n = n %self._size
        if n == 0:
            return
        new_data = [None] * 10
        for i in range(n):
            new_data[i] = self._data[(self._front + self._size - n + i) % 10]

        for i in range(self._size - n):
            new_data[n + i] = self._data[(self._front + i) % 10]

        self._data = new_data
        self._front = 0
        self._rear = self._size - 1

    def __str__(self):
        return f"Queue: {self._data}, front: {self._front}, rear: {self._rear}, size: {self._size}"

class FullQueueException(Exception):
    pass

class EmptyQueueException(Exception):
    pass


def basicFunctions():
    q = LimitedArrayQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("Originalni red: ")
    print(q)
    q.rotate(2)
    print("Red nakon rotacije: ")
    print(q)



basicFunctions()