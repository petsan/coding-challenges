class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        self.stack.append(val)
        if self.maxes:
            self.maxes.append(max(val, self.maxes[-1]))
        else: 
            self.maxes.append(val)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

myStack = MaxStack()

# myStack.pop()
myStack.push(3)
myStack.pop()
myStack.push(6)
myStack.push(4)
myStack.push(7)
myStack.push(5)

print(myStack.stack)
print(myStack.maxes)
