class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.left= None
        self.right= None

class BinaryTree:
    def __init__(self, data) -> None:
        self.root= Node(data)