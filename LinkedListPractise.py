class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)
    
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

sll = SinglyLinkedList()
sll.insert(1)
sll.insert(2)
sll.insert(3)
print(sll)

new_head = reverse_linked_list(sll.head)
sll.head = new_head
print(sll)

sll.delete(2)
print(sll)

index = sll.search(3)
print(index)
