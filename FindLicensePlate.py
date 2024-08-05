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
        for bucket in self._data:
            if bucket is not None:
                for key, value in bucket:
                    yield (key,value)
    
    def _bucket_getitem(self, index, key):
        bucket = self._data[index]
        if bucket is None:
            raise KeyError(f"Key Error: '{key}'")
        for k, v in bucket:
            if k == key:
                return v
            raise KeyError(f"Key Error: '{key}'")
    
    def _bucket_setitem(self, index, key, value):
        if self._data[index] is None:
            self._data[index] = []
        for i, (k,v) in enumerate(self._data[index]):
            if k == key:
                self._data[index][i] = (key, value)
                return
        self._data[index].append((key,value))
        self._size += 1
    
    def _bucket_delitem(self, index, key):
        bucket = self._data[index]
        if bucket is None:
            raise KeyError(f"Key Error: '{key}'")
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(f"Key Error: '{key}'")
    

def start_code():
    vehicles = {
    "ABC123": {"make": "Toyota", "model": "Corolla", "year": 2015},
    "XYZ789": {"make": "Honda", "model": "Civic", "year": 2018},
    "LMN456": {"make": "Ford", "model": "Focus", "year": 2020},
    "DEF101": {"make": "Tesla", "model": "Model 3", "year": 2021},
    }

    license_plate_map = HashMap()


    for plate, info in vehicles.items():
        license_plate_map[plate] = info 

    def run_license_plate(license_plate):
        try:
            info = license_plate_map[license_plate]
            return info
        except KeyError:
            return "Vehicle not found."
        
    print(run_license_plate("ABC123"))
    print(run_license_plate("XYZ789"))
    print(run_license_plate("NOEXIST"))

start_code()
        
