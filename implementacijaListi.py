class Node:
    def __init__(self, value, next):
        self._value = value
        self._next = next

    def get_node(self):
        return self._value
    
    def set_node(self, value):
        self._value = value
    
    def __str__(self):
        return f"Node(data: {self._value})"
    
    def __gt__(self, other):
        return self._value > other._value




class SingleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_Empty(self):
        return self._size == 0
    
    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node._next

    def append(self, value):
        new_node = Node(value, None)
        if self._head is None:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def get_first(self):
        if self.is_Empty():
            raise Exception("List is Empty")
        return self._head
    
    def get_last(self):
        if self.is_Empty():
            raise Exception("List is Empty")
        return self._tail
    
    def add_first(self, value):
        new_node = Node(value)
        if self.is_Empty():
            self._head = new_node
        else:
            new_node._next = self._head
        self._head = new_node
        self._size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.is_Empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_Empty():
            raise Exception("List is Empty")
        if self._size == 1:
            self._head = None
        self._head = self._head._next
        self._size -= 1

    def remove_last(self):
        if self.is_Empty():
            raise Exception("List is Empty")
        if self._size == 1:
            self._head = None
        for node in self:
            if node.next == self._tail:
                node.next = None
                self._tail = node
                break
        self._size -= 1

    def get_at(self, index):
        if not 0 <= index <= self._size-1:
            raise IndexError("Index out of range")
        counter = 0
        current_node = self._head
        while current_node:
            if counter == index:
                return current_node
            current_node = current_node._next
            counter += 1

    def insert_at(self, index, value):
        new_node = Node(value)
        if not 0 <= index <= self._size-1:
            raise IndexError("Index out of range")
        if index == 0:
            self.add_first(value)
            return
        previous_node = self.get_at(index-1)
        new_node._next = previous_node._next
        previous_node._next = new_node
        self._size += 1
    
    def remove_at(self, index):
        if not 0 <= index <= self._size-1:
            raise IndexError("Index out of range!")
        if index == 0:
            self.remove_first()
            return
        if index == self._size-1:
            self.remove_last()
            return
        previous_node = self.get_at(index-1)
        next_node = previous_node._next
        previous_node._next = next_node
        self._size -= 1



def find_max_in_list(lista):
    if not lista:
        raise Exception("List is Empty")
    return max(lista)

def sum_of_unique_el(lista):
    if not lista:
        raise Exception("List is Empty")
    elem_count = {}
    for node in lista:
        value = node.get_node()
        if value in elem_count:
            elem_count[value] += 1
        else:
            elem_count[value] = 1
    unique_elem = set()
    for value, count in elem_count.items():
        if count == 1:
            unique_elem.add(value)
    return sum(unique_elem)

l = SingleList()
l.append(2)
l.append(-1)
l.append(3)
l.append(6)
l.append(1)
l.append(5)
l.append(2)
l.append(5)
print(find_max_in_list(l))
print("Suma jedinstvenih brojeva: ", sum_of_unique_el(l))