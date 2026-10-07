## STACK USING LINKED LIST 
## linked list - No fixed capacity, nodes can be created dynamically 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top==None:
            print("Stack Underflow")
            return  
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return 
        value = self.top.data
        return value 

s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
print(s.peek())
s.pop()
print(s.pop())
print(s.peek())

