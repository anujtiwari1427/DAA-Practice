class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class StackLinkedList:

    def __init__(self):
        self.top = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        value = self.top.data
        self.top = self.top.next
        return value
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def display(self):
        temp = self.top

        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")
stack = StackLinkedList()
stack.push(100)
stack.push(200)
stack.push(300)

stack.display()

print("\nPopped:",stack.pop())
stack.display()
print("\nTop element:",stack.peek())
stack.display()