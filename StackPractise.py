class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflow("Stack underflow")
        else:
            self.size -= 1
            return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            raise StackUnderflow("Stack underflow")
        else:
            return self.stack[-1]
        
    def __iter__(self):
        return iter(self.stack)
    
    def is_balanced(self):
        for char in self:
            if char in ['(', '[', '{']:
                self.push(char)
            elif char in [')', ']', '}']:
                if self.is_empty():
                    return False
                self.pop()
        return self.is_empty()

class StackOverflow(Exception):
    pass

class StackUnderflow(Exception):
    pass

s = Stack()
s.push(")")
s.push(")")
s.push("(")
s.push("(")
print(s.is_empty())
print(s.peek())
print(s.is_balanced())
