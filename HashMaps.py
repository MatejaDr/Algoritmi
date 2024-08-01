import random


class HashMap(object):
    def __init__(self, capacity = 8):
        self._data = capacity * [None]
        self._capacity = capacity
        self._size = 0
        self.prime = 109345121
        self._a = 1 + random.randrange(self.prime-1)
        self._b = random.randrange(self.prime)

    def __len__(self):
        return self._size
    
    def _hash(self, x):
        hashed_value = (hash(x)*self._a+self._b) % self.prime
        return hashed_value % self._capacity
    
    def _resize(self, capacity):
        old_data = list(self.items())
        self._data = capacity * [None]
        self._size = 0
        for (k,v) in old_data:
            self[k] = v

    def __getitem__(self, key):
        bucket_index = self._hash(key)
        return self._bucket_getitem(bucket_index, key)
    
    def __setitem__(self, key, value):
        bucket_index = self._hash(key)
        self._bucket_setitem(bucket_index, key, value)
        current_capacity = len(self._data)
        if self._size > current_capacity //2:
            self._resize(2*current_capacity-1)
    
    def items(self):
        raise NotImplementedError()
    
    def _bucket_getitem(self, index, key):
        raise NotImplementedError()
    
    def _bucket_setitem(self, index, key):
        raise NotImplementedError()
    
    def _bucket_delitem(self, index, key):
        raise NotImplementedError()
        
