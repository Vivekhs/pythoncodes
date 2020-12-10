class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        del self.data[-1]

    def push(self, elem):
        self.data.append(elem)

    def display(self):
        for elem in self.data:
            print(elem)


stack = Stack()

stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()

stack.push(6)
stack.display()
