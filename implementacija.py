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

def isMatchedHTML(raw):
    s = ArrayStack()
    j = raw.find('<')
    while j !=-1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            s.push(tag)
        else:
            if s.is_empty:
                return False
            if tag[1:] != s.pop():
                return False
        j = raw.find('<', k+1)
    return s.is_empty        

izraz = '(11-2+3+(2*2))'
print(isMatched(izraz))
print(isMatchedHTML('<p><b>hello</b><p>'))
    