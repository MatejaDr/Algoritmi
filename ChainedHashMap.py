import random

class MapElement(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
    
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, new_key):
        self._key = new_key

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

class Map(object):
    def __init__(self):
        self.data = []

    def __getitem__(self, key):
        for item in self.data:
            if item.key == key:
                return item.value
        raise KeyError("Element with key %s doesn't exist." % str(key))
    
    def __setitem__(self, key, value):
        for item in self.data:
            if item.key == key:
                item.value = value
                return
        self.data.append(MapElement(key, value))

    def __delitem__(self, key):
        length = len(self.data)
        for i in range(length):
            if self.data[i].key == key:
                self.data.pop(i)
                return
        raise KeyError("Element with key %s doesn't exist." % str(key))
    
    def __len__(self):
        return len(self.data)
    
    def __contains__(self, key):
        for item in self.data:
            if item.key == key:
                return True
        return False
    
    def __iter__(self):
        for item in self.data:
            yield item.key

    def items(self):
        for item in self.data:
            yield item.key, item.value
    
    def keys(self):
        keys = []
        for key in self:
            keys.append(key)
        return keys
    
    def values(self):
        values = []
        for key in self:
            values.append(self[key])
        return values
    
    def clear(self):
        self.data = []

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

class ChainedHashMap(HashMap):
    def _bucket_getitem(self, index, key):
        bucket = self._data[index]
        if bucket is None:
            raise KeyError("There is no element with that key.")
        return bucket[key]
    
    def _bucket_setitem(self, bucket_index, key, value):
        bucket = self._data[bucket_index]
        if bucket is None:
            self._data[bucket_index] = Map()
        current_size = len(self._data[bucket_index])
        self._data[bucket_index][key] = value
        if len(self._data[bucket_index])>current_size:
            self._size += 1

    def _bucket_delitem(self, index, key):
        bucket = self._data[index]
        if bucket is None:
            raise KeyError("There is no element with that key.")
        del bucket[key]

    def __iter__(self):
        for bucket in self._data:
            if bucket is not None:
                for key in bucket:
                    yield key
    
    def items(self):
        for bucket in self._data:
            if bucket is not None:
                for key, value in bucket.items():
                    yield key,value

def run_chained_hash_map():
    chm = ChainedHashMap()
    chm.__setitem__(1, "one")
    chm.__setitem__(2, "two")
    chm.__setitem__(3, "three")
    
    print("Items in the Chained Hash Map:")
    for key, value in chm.items():
        print(f"{key}: {value}")
    
    print("\nGetting an item from the Chained Hash Map:")
    print(chm._bucket_getitem(chm._hash(3), 3))
    
    print("\nDeleting an item from the Chained Hash Map:")
    chm._bucket_delitem(chm._hash(1), 1)
    
    print("\nItems in the Chained Hash Map after deletion:")
    for key, value in chm.items():
        print(f"{key}: {value}")

run_chained_hash_map()