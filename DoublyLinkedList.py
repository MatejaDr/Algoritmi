class Node:
    def __init__(self, value, previous, next):
        self._value = value
        self._previous = previous
        self._next = next
    
    def get_value(self):
            return self._value

class DoublyLinkedList:
    def __init__(self):
        self._head = Node(None, None, None)
        self._tail = Node(None, self._head, None)
        self._head._next = self._tail
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def __iter__(self):
        current_node = self._head
        while current_node != self._tail:
            yield current_node
            current_node = current_node._next
    
    def get_first(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self._head._next
    
    def get_last(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self._tail._previous
    
    def add_first(self, value):
        new_node = Node(value, self._head, self._head._next)
        if self.is_empty():
            self._head._next = new_node
        else:
            new_node._previous = self._head
            #self._head._previous = new_node
            self._head = new_node
        self._size += 1
        return new_node
    
    def add_last(self, value):
        new_node = Node(value, self._head, self._head._next)
        if self.is_empty():
            self._tail._previous = new_node
        else:
            new_node._next = self._tail
            self._tail._previous = new_node
        self._size += 1
        return new_node
    
    def remove_first(self):
        if self.is_empty():
            raise EmptyList("List is empty")
        to_remove = self._head._next
        if self._size == 1:
            self._head._next = self._tail
            self._tail._previous = self._head
        else:
            new_first = Node(self._head._next, None, None)._next
            self._head = new_first
        self._size -= 1
        return to_remove
    
    def remove_last(self):
        if self.is_empty():
            raise EmptyList("List is empty")
        to_remove = self._tail._previous
        if self._size == 1:
            self._tail._previous = self._head
            self._head._next = self._tail
        else:
            second_last = self._tail._previous
            second_last = self._tail
            self._tail._previous = second_last
        self._size -= 1
        return to_remove
    
    def insert_after(self, node1, value):
        new_node = Node(value, None, None)
        node1 = new_node
        new_node._next = node1._next
        node1._next = new_node
        new_node._previous = node1
        self._size += 1
        return new_node
    
    def insert_before(self, node1, value):
        new_node = Node(value, None, None)
        node1 = new_node
        new_node._previous = node1._previous
        new_node._next = node1
        node1._previous = new_node
        self._size += 1
        return new_node
    
    def get_at(self, index):
        if not 0 <= index <= self._size-1:
            raise IndexError("Index out of range")
        current_node = self._head
        counter = 0
        while current_node != self._tail:
            if counter == index:
                return current_node
            current_node = current_node._next
            counter += 1

    def insert_at(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.add_first(value)
        if index == self._size:
            return self.add_last(value)
        current_node = self.get_at(index)
        new_node = self.insert_before(current_node, value)
        self._size+=1
        return new_node
    
    def remove_at(self, index):
        if not 0 <= index <= self._size-1:
            raise IndexError("Index out of range")
        if index == 0:
            return self.remove_first()
        previous_node = self.get_at(index-1)
        to_remove = Node(previous_node, None, None)._next
        next_node = Node(previous_node, None, None)._next
        Node(previous_node, None, None)._next = next_node
        self._size -= 1
        return to_remove



class EmptyList(Exception):
    pass

class IndexError(Exception):
    pass


dll = DoublyLinkedList()

dll.add_last(1)
dll.add_last(2)
dll.add_last(3)
dll.add_last(4)
dll.add_last(5)

print("Original list:")
for node in dll:
    print(node._value)

dll.insert_at(2, 10)
print("\nList after inserting 10 at index 2:")
for node in dll:
    print(node._value)

dll.remove_at(3)
print("\nList after removing element at index 3:")
for node in dll:
    print(node._value)

print("\nFirst element:", dll.get_first())
print("Last element:", dll.get_last())

dll.remove_first()
print("\nList after removing first element:")
for node in dll:
    print(node._value)

dll.remove_last()
print("\nList after removing last element:")
for node in dll:
    print(node._value)