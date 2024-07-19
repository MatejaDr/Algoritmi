class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
class BrowserHistory:
    def __init__(self):
        self.forward_stack = Stack()
        self.backward_stack = Stack()
        self.current = None

    def visit(self, url):
        if self.current:
            self.backward_stack.push(self.current)
        self.current = url
        self.forward_stack = Stack()

    def back(self):
        if not self.backward_stack.is_empty():
            self.forward_stack.push(self.current)
            self.current = self.backward_stack.pop()
            return self.current
        else:
            return None
    
    def forward(self):
        if not self.forward_stack.is_empty():
            self.backward_stack.push(self.current)
            self.current = self.forward_stack.pop()
            return self.current
        else:
            return None
        
    def get_current_url(self):
       return self.current
       """""
       if not self.backward_stack.is_empty():
           return self.backward_stack.peek()
       elif not self.forward_stack.is_empty():
           return self.forward_stack.peek()
       else:
           return None
        """


browser = BrowserHistory()
browser.visit("leetcode.com")
browser.visit("google.com")
browser.visit("facebook.com")
print(browser.get_current_url())
browser.back()
print(browser.get_current_url())
browser.back()
print(browser.get_current_url())
browser.forward()
print(browser.get_current_url())
browser.forward()
print(browser.get_current_url())
print(browser.forward())
print(browser.back())
