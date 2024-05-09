class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    

class tree:
    def __init__(self):
           self.root = None
    
    def insert(self,data):
        if not self.root:
            self.root = Node(data) 
            return
        else:
             self.insert_regretion(self.root,data)

    def insert_regretion(self,node,data):
        if data < node.data :
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_regretion(node.left,data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_regretion(node.right,data)
                

    def print_tree(self,node):
        if node:
            self.print_tree(node.left)
            print(node.data)
            self.print_tree(node.right)

t = tree()
t.insert(4)
t.insert(5)
t.insert(2)
t.insert(7)
t.insert(8)
t.insert(9)
t.insert(0)
t.insert(1)
t.insert(4)
t.print_tree(t.root)
