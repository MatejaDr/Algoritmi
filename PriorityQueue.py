class PQItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        return self.key < other.key
    
    def __le__(self, other):
        return self.key <= other.key
    
class PriorityQueue:
    def __init__(self):
        self._data = []

    def __len__ (self):
        return len(self._data)
    
    def __str__(self):
        return ', '.join('(%s, %s)' % (e.key, e.value) for e in self._data)
    
    def is_empty(self):
        return len(self) == 0
    
class PQError(Exception):
    pass

class UnsortedPriorityQueue(PriorityQueue):
    def __init__(self):
        super(UnsortedPriorityQueue, self).__init__()

    def find_min(self):
        if self.is_empty():
            raise PQError("Queue is empty.")
        min_item = self._data[0]
        size = len(self)
        for i in range(1, size):
            current_item = self._data[i]
            if current_item < min_item:
                min_item = current_item
        return min_item
    
    def min(self):
        min_item = self.find_min()
        return (min_item.key, min_item.value)
    
    def remove_min(self):
        min_item  = self.find_min()
        index = self._data.index(min_item)
        removed = self._data.pop(index)
        return removed.key, removed.value
    
    def add(self, key, value):
        new_item = PQItem(key, value)
        self._data.append(new_item)

def UnsortedPQTest():
    pq = UnsortedPriorityQueue()
    pq.add(3, "This value has key of 3")
    pq.add(4, "This value has key of 4")
    pq.add(5, "This value has key of 5")
    print(pq.__str__())
    print("Length: ", pq.__len__())
    print("Minimum key value is: ",pq.find_min().value)
    pq.remove_min()
    print(pq.__str__())
    pq.add(9, "This value has key of 9")
    print(pq.__str__())
    pq.add(7, "This value has key of 7")
    print(pq.__str__())
    pq.add(1, "This value has key of 1")
    print(pq.__str__())
    print("Minimum key value is: ",pq.find_min().value)

UnsortedPQTest()


