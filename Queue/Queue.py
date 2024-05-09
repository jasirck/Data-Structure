class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class stack():
    def __init__(self):
        self.head = None
    def  enqueue(self,data):
        new = node(data)
        if not self.head:
            self.head = new
            self.tail = self.head
        else:
            self.head.next = new

    def dequeue(self):
        if not self.head:
            return "no data"
        else:
            pop = self.head
            self.head = self.head.next
            return pop.data
        
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

s = stack()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.print()
print(s.dequeue(),'p')
print(s.dequeue(),'p')
print(s.dequeue(),'p')
s.print()