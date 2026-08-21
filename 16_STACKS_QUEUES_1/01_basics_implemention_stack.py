## STACK IS A DATA STRUCTURE TO STORE CERTAIN TYPE OF DATA , and performs push,pop,top,size operations on it - Follows the LIFO principle
## IMPLEMENTION OF STACK USING ARRAYS
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack)==0
    def display(self):
        return self.stack

s = Stack()
s.push(2)
s.push(3)
s.push(4)
print(s.top())
print(s.pop())
print(s.top())
print(s.display())


