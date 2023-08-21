class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self) -> None:
        self.head= None

    def add_at_begining(self, data):
        new_node= Node(data)
        new_node.next= self.head
        self.head= new_node

    def add_at_end(self, data):
        if self.head is None:
            self.add_at_begining(data)
        
        else:
            new_node= Node(data)
            n= self.head
            while n.next is not None:
                n= n.next
            n.next= new_node

    def insert(self, data, index):
        if self.head is None:
            self.add_at_begining(data)
        else:
            new_node= Node(data)
            n= self.head
            count= 1
            while count < index:
                n= n.next
                count += 1
            new_node.next= n.next
            n.next= new_node
    
    def remove(self, index):
        if self.head is None:
            print("The List is empty")
        
        else:
            count=1
            n= self.head
            while n:
                if count == index - 1:
                    n.next= n.next.next
                count += 1
                n= n.next
    
    def print(self):
        if self.head is None:
            print("The List is empty")
        
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n= n.next

l= LinkedList()
l.add_at_begining(5)
l.add_at_begining(50)
l.add_at_end(8)
l.add_at_end(88)
l.insert(0, 2)
l.print()