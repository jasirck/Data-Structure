class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_frant(self,data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def delete_first(self):
        if not self.head:
            print("no data")
        else:
            self.head = self.head.next

    def delete_end(self):
        if not self.head :
            print('no data')
        else:
            data = self.head
            while data.next.next is not None:
                data = data.next
            data.next = None

    def delete_value(self,data):
        if data == self.head.data:
            self.head = self.head.next
        x = self.head
        while x.next.next is not None:
            if x.next.data == data:
                break
            x = x.next
        if x.next is None:
            print("no data")
        else:
            x.next = x.next.next

    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            

li = Linked_list()
li.append(10)
li.append(11)
li.append(12)
li.append(13)
li.append(14)
li.append_frant(25)
li.delete_value(13)
# li.delete_end()
li.print_list()
a= li.middle()
print(a.data)
# li.delete_first()
