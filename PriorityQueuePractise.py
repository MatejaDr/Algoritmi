import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def is_empty(self):
        return not self._queue

    def extract_max(self):
        if self.is_empty():
            raise Exception("PQ is empty")
        return heapq.heappop(self._queue)[-1]
    
    def remove(self):
        if self.is_empty():
            raise Exception("PQ is empty")
        return heapq.heappop(self._queue)
    
pq = PriorityQueue()
pq.insert('item1', 5)
pq.insert('item2', 3)
pq.insert('item3', 8)
print(pq.extract_max())
pq.remove()
print(pq.extract_max())
