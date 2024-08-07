class HashMap(object):
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def __len__(self):
        return self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    self.handle_collisison(key_hash, key, value)
                    return True
            self.map[key_hash].append(key_value)
            return True
    
    def handle_collisison(self, key_hash, key, value):
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair.append(value)
                return True
        self.map[key_hash].append([key, value])
        return True

    def insert(self, index, key, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            self.map[key_hash] = [[key, value]]
        else:
            self.map[key_hash].insert(index, [key, value])

    def search(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1:]
        

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        for i in self.map:
            if i is not None:
                print(str(i))


hm = HashMap()
hm.add('apple', 5)
hm.add('apple', 11)
hm.add('banana', 4)
hm.add('pinapple', 7)
hm.print()
print()
hm.insert(1, 'pickle', 9)
hm.print()
print()
hm.delete('banana')
hm.print()
print()
print("Pronadjen: ", hm.search('apple'))
print(hm.print())