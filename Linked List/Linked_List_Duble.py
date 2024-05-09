class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublylist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new
            new.prev = current

    def print(self):
        current = self.head
        while current:
            print(current.data,)
            current = current.next

# Constructing a Doubly Linked List
doubly = doublylist()
doubly.append(1)
doubly.append(2)
doubly.append(3)
doubly.append(4)
doubly.append(5)
doubly.append(6)
doubly.print()
