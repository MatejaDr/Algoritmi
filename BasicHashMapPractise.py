class HashMap:
    def __init__(self, size = 10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def is_empty(self):
        return all(len(bucket) == 0 for bucket in self.buckets)

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return
            
hm = HashMap()
hm.put('key1', 5)
hm.put('key2', 7)
hm.put('key3', 3)
print(hm.get('key2'))
hm.remove('key3')
print(hm.get('key3'))