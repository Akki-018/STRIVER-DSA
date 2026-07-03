## Linked list stores element in nodes - every node has data and next - where next stores the address of the next element 
class Node:                   # Creating own datatype -  Node 
    def __init__(self,data):    # self - refers to the particular object 
        self.data = data
        self.next = None           
n1 = Node(5)
n2 = Node(15)
n3 = Node(25) 
n4 = Node(35)
head = n1
n1.next = n2
n2.next = n3
n3.next = n4 
n2.data = 50 
print(head.next.data)






        