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

    def visit(self, url):
        self.backward_stack.push(url)
        self.forward_stack = Stack()

    def back(self):
        if not self.backward_stack.is_empty():
            url = self.backward_stack.pop()
            self.forward_stack.push(url)
            return url
        else:
            return None
    
    def forward(self):
        if not self.forward_stack.is_empty():
            url = self.forward_stack.pop()
            self.backward_stack.push(url)
            return url
        else:
            return None
        
    def current_url(self):
        return self.backward_stack.peek()
    
browser = BrowserHistory()
browser.visit("leetcode.com")
browser.visit("google.com")
browser.visit("facebook.com")
print(browser.current_url())
browser.back()
print(browser.current_url())
browser.back()
print(browser.current_url())
browser.forward()
print(browser.current_url())
browser.forward()
print(browser.current_url())
