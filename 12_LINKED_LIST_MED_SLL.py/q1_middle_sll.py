## Return the linked list after the middle element 
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

# BRUTE FORCE - Find the number of elements in the sll and then traverse from the cnt - element to the end and return the sll 
def middle_sll_brute(head):
    cnt = 0 
    curr = head 
    while curr:
        cnt +=1 
        curr = curr.next 
    midd = cnt//2
    curr = head 
    for _ in range(midd):
        curr = curr.next 
    return curr 
curr = middle_sll_brute(head)
traversal_sll(curr)

def middle_sll_opt(head):
    slow = head
    fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
    return slow 
cur = middle_sll_opt(head)
traversal_sll(cur)


 
