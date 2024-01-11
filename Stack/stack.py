class Stack:
    def __init__(self):
        self.items= []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        if len(self.items) > 0:
            return True
        else:
            return False
    
    def display(self):
        return self.items

s= Stack()
s.push(5)
s.push(9)
s.display()
# s.pop()
s.display()
s.peek()
