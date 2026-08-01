## TO DETECT A LOOP IN A LINKED LIST
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

## BRUTE FORCE - TC - o(n),SC-o(n)
# APPROACH - we store every NODE in a set and while traversing we check if the node is in the set and if yes we return True- otherwise we add this element in the set and traverse forward 

def linked_list_cycle(head):
    vis = set()
    curr = head 
    while curr:
        if curr in vis:
            return True
        vis.add(curr)
        curr = curr.next
    return False
print(linked_list_cycle(head))

## OPTIMAL APPROACH - Two pointer approach 
def linked_list_cycle_opt(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
print(linked_list_cycle_opt(head))

