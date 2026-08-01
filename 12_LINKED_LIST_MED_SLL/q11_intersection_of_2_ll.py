## TO RETURN THE NODE Which is the intersection of two linked list 
# SINGLY LINKED LIST 
# CREATING A SINGLY LINKED LIST 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n2 = Node(25)
n3 = Node(30)
n4 = Node(35)
n5 = Node(5)
n6 = Node(10)
n7 = Node(15)
n8 = Node(30)
n9 = Node(35)
head1 = n2
n2.next = n3
n3.next = n4
head2 = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9 

# TRAVERSAL IN A SLL 
def traversal_sll(head):
    curr = head 
    while curr:
        print(curr.data , end = " <-> ")
        curr = curr.next
    print(None)

# BRUTE APPROACH - TC -o(n^2), SC - O(1)
def intersection_brut(head1,head2):
    curr1 = head1
    curr2 = head2
    while curr1:
        curr2 = head2 
        while curr2:
            if curr1==curr2:
                return curr1
            curr2 = curr2.next
        curr1 = curr1.next 
    return None 
print(intersection_brut(head1,head2))

## BETTER APPROACH - TC - o(n),SC - o(n)
def intersection_bett(head1,head2):
    seen = set()
    curr1 = head1
    curr2 = head2
    while curr1:
        seen.add(curr1)
        curr1 = curr1.next 
    while curr2:
        if curr2 in seen:
            return curr2
        curr2 = curr2.next 
    return None 
print(intersection_bett(head1,head2))
