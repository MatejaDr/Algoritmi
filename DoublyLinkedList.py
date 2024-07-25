class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head.next
        while current:
            yield current.value
            current = current.next

    def clear(self):
        self.head = Node(None)
        self.tail = self.head
        self.size = 0

    def is_empty(self):
        return self.head == None

    def get_element(self, index):
        current = self.head.next
        count = 0
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if not self.head.next:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail.prev = new_node
            new_node.next = self.tail
        else:
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
        self.size += 1

    def get_first(self):
        if self.is_empty():
            raise EmptyList("List is empty")
        return self.head.next.value
    
    def get_last(self):
        if self.is_empty():
            raise EmptyList("List is empty")
        return self.tail.prev.value

    def add_first(self, value):
        new_node = Node(value)
        if not self.head.next:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail.prev = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.head.next
            self.head.next.prev = new_node
            new_node.prev = self.head
            self.head.next = new_node
        self.size += 1

    def insert_after(self, value, index):
        if self.is_empty():
            raise EmptyList("List is empty")
        elif index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        else:
            new_node = Node(value)
            current = self.head.next
            count = 0
            while current:
                if count == index:
                    new_node.next = current.next
                    if current.next:
                        current.next.prev = new_node
                    else:
                        self.tail.prev = new_node
                    current.next = new_node
                    new_node.prev = current
                    self.size+=1
                    return
                count +=1
                current = current.next

    def insert_before(self, value, index):
        if self.is_empty():
            raise EmptyList("List is empty")
        elif index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        else:
            new_node = Node(value)
            if index == 0:
                new_node.next = self.head.next
                self.head.next.prev = new_node
                self.head.next = new_node
                new_node.prev = self.head
            else:
                current = self.head.next
                count = 0
                while current:
                    if count == index-1:
                        new_node.next = current.next
                        current.next.prev = new_node
                        current.next = new_node
                        new_node.prev = current
                        break
                    count += 1
                    current = current.next
            self.size += 1


    def insert_at(self, value, index):
        new_node = Node(value)
        if self.is_empty():
            self.head.next = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
        else:
            current = self.head.next
            count = 0
            while current:
                if count == index-1:
                    new_node.next = current.next
                    if current.next:
                        current.next.prev = new_node
                    else:
                        self.tail = new_node
                    current.next = new_node
                    new_node.prev = current
                    break
                count += 1
                current = current.next
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise EmptyList("Prazna lista")
        else:
            to_remove = self.head.next
            if self.size == 1:
                self.head.next = None
                self.tail = self.head
            else:
                new_first = self.head.next.next
                new_first.prev = self.head
                self.head.next = new_first
            self.size -= 1
            return to_remove.value

    def remove_last(self):
        if self.is_empty():
            raise EmptyList("Prazna lista")
        else:
            to_remove = self.tail.prev
            if self.size == 1:
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                new_last = to_remove.prev
                new_last.next = self.tail
                self.tail.prev = new_last
            self.size -= 1
            return to_remove.value

    def remove_at(self, index):
        if self.is_empty():
            raise EmptyList("List is empty")
        else:
            if index == 0:
                return self.remove_first()
            elif index == self.size-1:
                return self.remove_last()
            else:
                current = self.head.next
                count = 0
                while current:
                    if count == index-1:
                        to_remove = current.next
                        next_node = current.next.next
                        current.next = next_node
                        if next_node:
                            next_node.prev = current
                        else:
                            self.tail = current
                        self.size -= 1
                        return to_remove.value
                    count += 1
                    current = current.next

    def update(self, index, new_value):
        current = self.head.next
        count = 0
        while current:
            if count == index:
                current.value = new_value
                return
            count += 1
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print()

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print()

class EmptyList(Exception):
    pass

class IndexError(Exception):
    pass

def TestCode():
    dll = DoublyLinkedList()
    dll.append(15)
    dll.append(25)
    dll.append(35)
    print(dll.get_element(3))
    dll.add_first(7)
    dll.update(2, 100)
    dll.update(3, 200)
    print(dll.get_element(0))
    dll.remove_at(1)
    dll.display()
    dll.insert_at(99, 1)
    dll.remove_first()
    dll.display()
    dll.add_first(70)
    print(dll.get_element(0))
    dll.display()
    dll.append(300)
    dll.display()
    dll.clear()
    dll.display()

def TestCodeVTWO():
    dll = DoublyLinkedList()
    dll.append(15)
    dll.append(25)
    dll.append(35)
    dll.display()
    dll.remove_last()
    dll.display()
    dll.append(30)
    dll.display()
    dll.insert_after(20, 0)
    dll.display()
    dll.insert_before(27, 3)
    dll.display()
    dll.display_backward()
    

TestCodeVTWO()