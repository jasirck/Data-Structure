class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
        

    def array_to_list(self, arr):
        for i in arr:
            node = Node(i)
            if not self.head:
                self.head = node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = node

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list = LinkedList()

arr = [1, 2, 3, 4, 5]
linked_list.array_to_list(arr)

linked_list.print()
