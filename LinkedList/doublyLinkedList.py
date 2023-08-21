class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.next= None
        self.prev= None

class DLinkedList:
    def __init__(self) -> None:
        self.head= None
    
    def add_at_begin(self, data):
        new_node= Node(data)
        new_node.next= self.head
        self.head= new_node
        new_node.prev= self.head

    def add_at_end(self, data):
        if self.head is None:
            self.add_at_begin(data)

        else:
            new_node= Node(data)
            n= self.head
            while n.next is not None:
                n= n.next
            n.next= new_node
            new_node.prev= n
            
    def insert(self, data, index):
        if self.head is None:
            self.add_at_begin(data)

        else:
            new_node= Node(data)
            n= self.head
            count= 0
            while count== index:
                n= n.next
                count+= 0
            n.next.prev= new_node
            new_node.next= n.next
            n.next= new_node
            new_node.prev= n

    def remove(self, index):
        if self.head is None:
            print("The list is empty")
        else:
            n= self.head
            count= 1
            while count!= index:
                count+=1
                n= n.next
            n.next= n.next.next
            n.next.prev= n
            
    
    def print(self):
        if self.head is None:
            print("The list is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n= n.next

l= DLinkedList()
l.add_at_begin(5)
l.add_at_begin(50)
l.add_at_end(0)
l.add_at_end(10)
l.insert(1,2)
l.remove(1)
l.print()