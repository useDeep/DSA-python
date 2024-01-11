class Queue:
    def __init__(self) -> None:
        self.items= []

    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        self.items.pop(0)

    def peek(self):
        return self.items[-1]
    
    def print(self):
        print(self.items)
    
q= Queue()
q.enqueue(5)
q.enqueue(55)
q.enqueue(50)
q.dequeue()
q.print()