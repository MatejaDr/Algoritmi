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

def MapTest():
    m = Map()
    m.__setitem__(1, 'a')
    m.__setitem__(2, 'b')
    m.__setitem__(3, 'c')
    m.__setitem__(4, 'd')
    print(m.keys())
    print(m.values())
    if m.__contains__(5):
        print("Map does contain key of 5")
    else:
        print("Map does not contain key of 5")
    m.__delitem__(2)
    print(m.keys())
    print(m.values())
    print(m.__len__())
    m.clear()
    print(m.__len__())

MapTest()