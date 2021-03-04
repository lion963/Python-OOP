class Stack():
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.insert(0, item)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        result = "["
        result += f"{', '.join(self.data)}"
        result += "]"
        return f'{result}'


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))
