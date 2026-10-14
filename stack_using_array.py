class StackArray:

    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            print("Underflow")
        else:
            return self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def display(self):
        print("Stack:",self.stack)
SA = StackArray()
SA.push(10)
SA.push(20)
SA.push(30)
SA.display()
print("\nAfter delete element:")
SA.pop()
SA.display()
print("\nTop element:")
SA.peek()
SA.display()
