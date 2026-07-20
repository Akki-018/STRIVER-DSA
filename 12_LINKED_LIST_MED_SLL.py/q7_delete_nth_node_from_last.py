## TO DELETE THE Nth NODE FROM THE LAST OF THE LINKED LIST 
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

## BRUTE FORCE - TC - o(n), SC - o(1)
def delete_nth(head,n):
    if not head or not head.next:
        return None
    cnt = 0 
    curr = head
    while curr:
        cnt+=1
        curr = curr.next 
    n = cnt-n+1
    if n==1:
        return head.next 
    a = 1
    curr = head 
    while curr:
        if a == n-1:
            curr.next = curr.next.next
            break 
        curr = curr.next
        a+=1
    return head 
head = delete_nth(head,2)
traversal_sll(head)