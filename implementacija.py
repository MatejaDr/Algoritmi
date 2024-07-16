class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    @property
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty:
            raise Exception("Stack is empty")
        return self.data[-1]
    
    def pop(self):
        if self.is_empty:
            raise Exception("Stack is empty")
        return self.data.pop()
    
def isMatched(exp):
    lefty = '({['
    righty = ')}]'
    s = ArrayStack()
    for c in exp:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty:
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty

izraz = '(11-2+3+(2*2))'
print(isMatched(izraz))
    