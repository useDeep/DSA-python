class Node:
    def __init__(self, data= None) -> None:
        self.data= data
        self.next= None

class CLinkedList:
    def __init__(self) -> None:
        self.head= None
    
    def add_at_begining(self, data):
        if self.head is None:
            new_node= Node(data)
            self.head= new_node
            new_node.next= self.head
        
        else:
            new_node= Node(data)
            new_node.next= self.head
            self.head= new_node