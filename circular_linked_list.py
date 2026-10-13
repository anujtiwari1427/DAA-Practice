class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
class CirLinList:

    def __init__(self):
        self.head = None
    
    def insert_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head

        while temp.next!= self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_pos(self,pos,data):
        if pos == 1:
            self.insert_beg(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(pos - 2):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node        
    
    def delete_beg(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    def delete_end(self):

        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head

        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("(Head)")

cll = CirLinList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

print("Circular Linked List:")
cll.display()

cll.insert_beg(5)
print("\nInserted beginning: ")
cll.display()
cll.insert_pos(3,15)
print("\nInserted at position 3: ")
cll.display()

cll.delete_end()
print("\nDelete from end: ")

cll.display()
