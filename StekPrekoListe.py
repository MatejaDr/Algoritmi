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

class Stack:
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        return self._head == None
    
    def push(self, value):
        if self._head == None:
            self._head = Node(value, None)
        else:
            newnode = Node(value, self._head)
            newnode._next = self._head
            self._head = newnode

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self._head._value
            self._head = self._head._next
            return value
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self._head._value
    
    def display(self):
        iternode = self._head
        if self.is_empty():
            print("Stack underflow")
        else:
            while iternode != None:
                print(iternode._value, end = "")
                iternode = iternode._next
                if iternode != None:
                    print("->", end = "")
            return
        
def stackUsingLists():
    s = Stack()
    s.push(11)
    s.push(22)
    s.push(33)
    s.push(44)
    s.display()
    print("\nTop element is ", s.peek())
    s.pop()
    s.pop()
    s.display()
    print("\nTop element is ", s.peek())

stackUsingLists()