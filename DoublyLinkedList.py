class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head == None

    def get_element(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_first(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at(self, value, index):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
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

    def remove_first(self):
        if self.is_empty():
            raise EmptyList("Prazna lista")
        else:
            to_remove = self.head.next
            if self.size == 1:
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                new_first = self.head.next.next
                new_first.prev = self.head
                self.head.next = new_first
            self.size -= 1
            return to_remove

    def remove_last(self):
        if self.is_empty():
            raise EmptyList("Prazna lista")
        else:
            to_remove = self.tail.prev
            if self.size == 1:
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                new_last = self.tail.prev.prev
                new_last.next = self.tail
                self.tail.prev = new_last
            self.size -= 1
            return to_remove

    def display(self):
        print("None", end=" <-> ")
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

class EmptyList(Exception):
    pass

class IndexError(Exception):
    pass

def TestCode():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.add_first(7)
    dll.insert_at(8, 2)
    print(dll.get_element(0))
    dll.display()
    #dll.remove_first()
    #dll.add_last(10)
    #dll.display()
    #dll.remove_last()
    #dll.display()
    #print(dll.is_empty())
    #dll.insert_before(11, 10)
    #dll.display()

TestCode()