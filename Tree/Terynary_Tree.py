class treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.middle = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = treenode(data)
        else:
            self.insert_regretion(self.root,data)

    def insert_regretion(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = treenode(data)
            else:
                self.insert_regretion(node.left,data)
        elif data ==  node.data:
            if  node.middle is None:
                node.middle = treenode(data)
            else:
                self.insert_regretion(node.middle,data)
        else:
            if node.right is None:
                node.right = treenode(data)
            else:
                self.insert_regretion(node.right,data)

    def print_tree(self, node):
        if node:
            self.print_tree(node.left)
            print(node.data)
            self.print_tree(node.middle)
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
