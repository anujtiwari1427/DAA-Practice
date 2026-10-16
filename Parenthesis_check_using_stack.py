def check_balanced(expression):
    stack = []
    for char in expression:

        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


expression = input("Enter an expression: ")


if check_balanced(expression):
    print("Parentheses are Balanced")
else:
    print("Parentheses are Not Balanced")



