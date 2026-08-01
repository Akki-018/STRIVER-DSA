## TO merge two sorted lists and return the sorted list 
# SINGLY LINKED LIST 
# CREATING A SINGLY LINKED LIST 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(20)
n2 = Node(25)
n3 = Node(30)
n4 = Node(5)
n5 = Node(10)
n6 = Node(15)
head1 = n1
n1.next = n2
n2.next = n3
head2 = n4
n4.next = n5
n5.next = n6

# TRAVERSAL IN A SLL 
def traversal_sll(head):
    curr = head 
    while curr:
        print(curr.data , end = " <-> ")
        curr = curr.next
    print(None)

## SOLUTION 
def merge_sorted_lists(head1,head2):
    dummy = Node(-1)
    tail = dummy
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        if curr1.data<=curr2.data:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next 
    if curr1:
        tail.next = curr1
    else:
        tail.next = curr2
    return dummy.next
head = merge_sorted_lists(head1,head2)
traversal_sll(head)