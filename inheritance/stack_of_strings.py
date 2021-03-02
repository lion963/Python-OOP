class Stack():
    def __init__(self):
        self.data=[]

    def push(self, item):
        self.data.insert(0, item)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data.pop()


    def is_empty(self):
        return True if self.data else False

class str(str, Stack):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

    def __repr__(self):
        result="["
        result+=f"{', '.join(self.obj.data)}"
        result+="]"
        return result


# stack = Stack()
# stack.push("apple")
# stack.push("carrot")
# print(str(stack))


# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.peek(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()