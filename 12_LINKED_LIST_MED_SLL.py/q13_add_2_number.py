## TWO ADD 2 linked list  -- LC (2)
# SINGLY LINKED LIST 
# CREATING A SINGLY LINKED LIST 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(2)
n2 = Node(4)
n3 = Node(3)
n4 = Node(5)
n5 = Node(6)
n6 = Node(4)
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

## OPTIMAL APPROACH 
def add_2_ll(head1,head2):
    dummy = Node(-1)
    tail = dummy
    curr1 = head1
    curr2 = head2 
    carry = 0 
    while curr1 or curr2 or carry :
        total = carry 
        if curr1:
            total+=curr1.data
        if curr2:
            total+=curr2.data

        digit = total%10
        carry = total//10

        new_node = Node(digit)
        tail.next = new_node
        tail = tail.next

        if curr1:
            curr1 = curr1.next 
        if curr2:
            curr2 = curr2.next 
    return dummy.next 
head = add_2_ll(head1,head2)
traversal_sll(head)

