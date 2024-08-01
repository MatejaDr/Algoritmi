class PQItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        return self.key < other.key
    
    def __le__(self, other):
        return self.key <= other.key

    def __str__(self):
        return f'({self.key}, {self.value})'
    
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

def simulate_hospital_queue():
    pq = UnsortedPriorityQueue()    
    pq.add(1, "Alex")
    pq.add(3, "Charlie")
    pq.add(1, "Alice")
    pq.add(2, "Bob")

    print(pq.__str__())

    while not pq.is_empty():
        priority, patient = pq.remove_min()
        print(f"Patient {patient} has priority {priority}")

simulate_hospital_queue()
