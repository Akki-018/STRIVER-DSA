## WE HAVE TO RETURN THE SORTED LIST 
# SINGLY LINKED LIST 
# CREATING A SINGLY LINKED LIST 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
n1 = Node(20)
n2 = Node(15)
n3 = Node(5)
n4 = Node(25)
n5 = Node(10)
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

## BRUTE FORCE - TC - o(nlogn), SC - o(1)
def sort_list_brute(head):
    if not head:
        return None
    curr = head 
    arr = []
    while curr:
        arr.append(curr.data)
        curr = curr.next
    arr.sort()
    curr = head
    i=0
    while curr:
        curr.data = arr[i]
        i+=1
        curr = curr.next
    return head
head = sort_list_brute(head)
traversal_sll(head)