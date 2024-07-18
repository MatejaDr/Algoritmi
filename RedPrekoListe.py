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

class Queue:
    def __init__(self):
        self._front = self._rear = None
        
    def is_empty(self):
        return self._front == None
    
    def enqueue(self, value):
        temp = Node(value)
        if self._rear == None:
            self._front = self._rear = temp
            return
        self._rear._next = temp
        self._rear = temp

    def dequeue(self):
        if self.is_empty():
            return 
        temp = self._front
        self._front = temp._next
        if self._front == None:
            self._rear = None