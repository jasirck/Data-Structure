class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
    
    def append (self,node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node    

    def insetfrant(self,node):
        node.next = self.head
        self.head = node

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


lils = LinkedList()
lils.append(Node(1))
lils.append(Node(2))
lils.append(Node(3))
lils.append(Node(4))
lils.append(Node(6))
lils.print()
