## TO ADD 1 to a number in a linked list 
# SINGLY LINKED LIST 
# CREATING A SINGLY LINKED LIST 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
head = n1
n1.next = n2
n2.next = n3 
n3.next = n4
n4.next = n5

# TRAVERSAL IN A SLL 
def traversal_sll(head):
    curr = head 
    while curr:
        print(curr.data , end = " <-> ")
        curr = curr.next
    print(None)
traversal_sll(head)

# Approach-1 --> REVERSE - ADD - REVERSE 
def reverse(head):
    prev = None 
    curr = head 
    while curr:
        next_node = curr.next 
        curr.next = prev 
        prev = curr
        curr = next_node
    return prev 

def add_1_ll_1(head):
    head = reverse(head)
    
    curr = head
    carry = 1 
    while curr and carry:
        total = curr.data + carry
        curr.data = total%10
        carry = total//10
        if carry == 0:
            break 
        if curr.next is None:
            curr.next = Node(carry)
            carry = 0 
            break
        curr = curr.next 

    head = reverse(head)
    return head 
    
head = add_1_ll_1(head)
traversal_sll(head)


        


