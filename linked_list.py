class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_position(self,pos,data):

        if pos == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(pos - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def delete_beginning(self):

        if self.head is None:
            return
        self.head = self.head.next

    def delete_end(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def search(self,key):

        temp = self.head

        while temp:

            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head

        while temp:
            print(temp.data,end="->")
            temp = temp.next

        print("None")

sll = SinglyLinkedList()

sll.insert_beginning(20)
sll.insert_beginning(10)
sll.insert_end(30)
sll.insert_end(40)
print("Linked List:","\n",sll.display())
sll.insert_position(3,25)
sll.display()
sll.delete_beginning()
sll.display()
sll.delete_end()
sll.display()

if sll.search(25):
    print("25 Found")
else:
    print("Not Found")



