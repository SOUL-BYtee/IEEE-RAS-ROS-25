class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def display(self):
        return self.items

    def is_empty(self):
        return len(self.items) == 0


# Example 
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("Stack items:", stack.display())
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())
print("Stack items:", stack.display())