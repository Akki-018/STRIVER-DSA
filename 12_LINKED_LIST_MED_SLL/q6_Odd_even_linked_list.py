## To return the list in a segragated manner- with nodes at odd indices first and then followed with  even indices 
# SINGLY LINKED LIST 
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
        print(curr.data , end = " <-> ")
        curr = curr.next
    print(None)
traversal_sll(head)

## Optimal solution - TC-o(n),Sc-o(1)
def odd_even_ll(head):
    if not head :
        return None 
    odd = head 
    even = head.next
    eve_head = even
    while even and even.next:
        odd.next = even.next 
        odd = odd.next 
        even.next = odd.next 
        even = even.next
    odd.next = eve_head
    return head
head = odd_even_ll(head)
traversal_sll(head)
