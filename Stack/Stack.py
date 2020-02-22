# Custom Exception
class StackException(Exception):
    pass


class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        try:
            if (len(self.stack) is self.max_size):
                raise StackException("Stack Overflow")
        except StackException as msg:
            print(msg)
        else:
            self.stack.append(item)

    def pop(self):
        try:
            if (len(self.stack) is 0):
                raise StackException("Stack Underflow")
        except StackException as msg:
            print(msg)
            print("Cannot delete from empty stack")
        else:
            print("Popped", self.stack[-1], "from the stack")
            self.stack.pop()

    def Print(self):
        try:
            if (len(self.stack) is 0):
                raise StackException("Stack Underflow")
        except StackException as msg:
            print(msg)
            print("Stack hence cannot be printed")
        else:
            print(self.stack)


# Driver Code
if __name__ == '__main__':
    stack = Stack(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.Print()
    stack.pop()
    stack.Print()
    stack.pop()
    stack.Print()
    stack.pop()
