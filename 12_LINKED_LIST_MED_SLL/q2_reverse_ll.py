## REVERSE THE GIVEN LINKED LIST 
# CREATING A SINGLY LINKED LIST 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
n5 = Node(25)
head = n1
n1.next = n2
n2.next = n3 
n3.next = n4
n4.next = n5

# TRAVERSAL IN A SLL 
def traversal_sll(head):
    curr = head 
    while curr:
        print(curr.data , end = " -> ")
        curr = curr.next
    print(None)
traversal_sll(head)
# ITERATIVE METHOD 
def reverse_ll(head):
    prev = None
    curr = head 
    while curr:
        next_node = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next_node
    return prev 
a = reverse_ll(head)
traversal_sll(a)

# RECURSIVE APPROACH 
def reverse_lll(head):
    def reverse(head):
        if (head==None or head.next==None):
            return head 
    new_head = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head
a = reverse_lll(head)
traversal_sll(head)
