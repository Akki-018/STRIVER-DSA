# To find the starting node of the the cycle in the linked list 
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

## BRUTE FORCE - TC - o(n), SC-o(n) 
def linked_list_brute(head):
    vis = set()
    curr = head
    while curr:
        if curr in vis:
            return curr
        vis.add(curr)
        curr = curr.next 
    return None 
print(linked_list_brute(head))

## OPTIMAL APPROACH - TC -o(n),Sc-o(1)
def linked_list_opt(head):
    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow==fast:
            break
    if not fast.next or not fast:
        return None
    slow = head 
    while slow!=fast:
        slow = slow.next
        fast = fast.next 
    return slow
print(linked_list_opt(head))