class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class stack():
    def __init__(self):
        self.head = None
    def  push(self,data):
        new = node(data)
        if not self.head:
            self.head = new
            self.tail = self.head
        else:
            new.next = self.head
            self.head = new

    def pop(self):
        if not self.head:
            return "no data"
        else:
            pop = self.head
            self.head = self.head.next
            return pop.data
    def is_empty(self):
        return not self.head

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

def reverce(old):
    s = stack()
    while not old.is_empty():
        s.push(old.pop())
    return s

s = stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.print()
k = reverce(s)
k.print()