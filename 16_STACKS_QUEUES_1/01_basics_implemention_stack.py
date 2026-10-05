## STACK IS A DATA STRUCTURE TO STORE CERTAIN TYPE OF DATA , and performs push,pop,top,size operations on it - Follows the LIFO principle
## IMPLEMENTION OF STACK USING ARRAYS
class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None]*size
        self.top = -1

    def push(self,val):
        if self.top == self.size -1 :
            print("Stack OVerflow")
            return 
        self.top = self.top+1
        self.stack[self.top] = val

    def pop(self):
        if self.top == -1 :
            print("Stack Underflow")
            return 
        value = self.stack[self.top]
        self.top-=1
        return value
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return 
        return self.stack[self.top]
    def isEmpty(self):
        return self.top==-1 
    def isFull(self):
        return self.top == self.size -1 

s = Stack(5)
s.push(5)
s.push(10)
s.push(15)
print(s.peek())
s.pop()
print(s.peek())

    