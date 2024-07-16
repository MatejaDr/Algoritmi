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
    
def isMatched(exp): # Funkcija za proveru uparivanja obicnih zagrada
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

def isMatchedHTML(raw): # Funkcija za proveru uparivanja HTML zagrada
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

class FullStackException(Exception): 
    pass

class LimitedStack: # Klasa Stack sa ogranicenjem, gde se pri definisanju stacka moze dodeliti velicina
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
    
    def __len__(self):
        return len(self.data)
    
    @property
    def is_empty(self):
        return len(self.data) == 0
    
    def is_full(self):
        return len(self.data) >= self.capacity

    def push(self, e):
        if self.is_full:
            raise FullStackException("Stack je pun.")
        self.data.append(e)


    def top(self):
        if self.is_empty:
            raise Exception("Stack is empty")
        return self.data[-1]
    
    def pop(self):
        if self.is_empty:
            raise Exception("Stack is empty")
        return self.data.pop()

def dodajStringUStek(stack, string): # Funkcija koja dodaje karaktere datog stringa u stack
    try:
        for i in string:
            stack.push(i)
    except FullStackException as e:
        print(e)

def isPalindrome(string): # Funkcija proverava da li je dati string palindrom, koristeci stack
    s = ArrayStack()
    n = []
    dodajStringUStek(s, string)
    while not s.is_empty:
        n.append(s.pop())
    provera = ''.join(n)
    nova_provera = provera.replace(" ", "").replace(",", "").lower()
    nova_rec = string.replace(" ", "").replace(",", "").lower()
    if nova_provera == nova_rec:
        print("Data rec je palindrom")
    else:
        print("Data rec nije palindrom")

def obrniString(string):
    s = ArrayStack()
    dodajStringUStek(s, string)
    while not s.is_empty:
        print(s.pop())

rec = "A man, a plan, a canal, Panama"
isPalindrome(rec)
obrniString(rec)



