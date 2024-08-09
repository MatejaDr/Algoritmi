class ArrayQueue:
    def __init__(self):
        self._items = []
        self._size = 0
        self._front = 0
        self._rear = -1
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, value):
        if not self.is_empty():
            self._items.append(value)
            self._rear += 1
            self._size += 1
        else:
            self._items = [value]
            self._rear = 1
            self._size = 1

    def dequeue(self):
        if not self.is_empty():
            item = self._items.pop(0)
            self._size -= 1
            return item
        else:
            raise EmptyQueueException("Queue is empty")
    
    def front(self):
        if not self.is_empty():
            return self._items[self._front]
        else:
            raise EmptyQueueException("Queue is empty")

class LimitedArrayQueue:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._size = 0
        self._front = 0
        self._rear = -1

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == len(self._items)

    def enqueue(self, value):
        if not self.is_full():
            self._rear = (self._rear + 1) % len(self._items)
            self._items[self._rear] = value
            self._size += 1
        else:
            raise FullQueueException("Queue is full")
        
    def dequeue(self):
        if not self.is_empty():
            item = self._items[self._front]
            self._front = (self._front + 1) % len(self._items)
            self._size -= 1
            return item
        else:
            raise EmptyQueueException("Queue is empty")
        
    def front(self):
        if not self.is_empty():
            return self._items[self._front]
        
class FullQueueException(Exception):
    pass

class EmptyQueueException(Exception):
    pass

def MainCodeForArrayQueue():
    aq = ArrayQueue()
    aq.enqueue(1)
    aq.enqueue(2)
    aq.enqueue(3)
    aq.enqueue(4)
    aq.enqueue(5)

    print("ArrayQueue size: ", len(aq))
    print("Front of ArrayQueue: ", aq.front())

    print("Dequeued item: ", aq.dequeue())

    print("ArrayQueue size: ", len(aq))
    print("Front of ArrayQueue: ", aq.front())
    print()
    print()

def MainCodeForLimitedArrayQueue():
    laq = LimitedArrayQueue(3)
    laq.enqueue(10)
    laq.enqueue(20)
    laq.enqueue(30)

    print("LimitedArrayQueue size: ", len(laq))
    print("Front of LimitedArrayQueue: ", laq.front())

    try:
        laq.enqueue(40)
    except FullQueueException as e:
        print(e)

    print("Dequeued item: ", laq.dequeue())

    print("LimitedArrayQueue size: ", len(laq))
    print("Front of LimitedArrayQueue: ", laq.front())

    try:
        laq.dequeue()
        laq.dequeue()
        laq.dequeue()
        laq.dequeue()
        laq.dequeue()
    except EmptyQueueException as e:
        print(e)

MainCodeForArrayQueue()
MainCodeForLimitedArrayQueue()