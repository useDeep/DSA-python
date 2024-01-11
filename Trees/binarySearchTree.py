class BST:
    def __init__(self, key= None) -> None:
        self.key= key
        self.lchild= None
        self.rchild= None

    def insert(self, data):
        if self.key is None:
            self.key= data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild= BST(data)
        else:    
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild= BST(data)

    def search(self, data):
        if self.key is None:
            print("tree empty")
            return
        if self.key== data:
            print("Found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("not found")
    
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key, end=" ")

    def delete(self, data):
        if self.key is None:
            print("tree is empty")
            return
        if self.key > data:
            if self.lchild:
                self.lchild= self.lchild.delete(data)
            else:
                print("node is not present")
        elif self.key < data:
            if self.rchild:
                self.rchild= self.rchild.delete(data)
            else:
                print("node is not present")
        else:
            if self.lchild is None:
                temp= self.rchild
                self= None
                return temp
            if self.rchild is None:
                temp= self.lchild
                self= None
                return temp
            node= self.rchild
            while node.lchild:
                node= self.lchild
            self.key= node.key
            self.rchild= self.rchild.delete(node.key)
        return self


x= BST()
l= [1,0, 7, 5, 2, 8, 6]
for i in l:
    x.insert(i)
x.preorder()
print("\ndeleted")
x.delete(7)
x.preorder()
