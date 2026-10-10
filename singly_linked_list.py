class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_beg(self,data):
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


