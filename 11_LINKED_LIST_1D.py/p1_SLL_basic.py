### Linked list stores element in nodes - every node has data and next - where next stores the address of the next element 
## SINGLY LINKED LIST 
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
        print(curr.data)
        curr = curr.next
traversal_sll(head)

# COUNT OF THE NUMBER OF NOES IN AN SLL 
def count_sll(head):
    curr = head 
    cnt = 0
    while curr:
        cnt+=1
        curr = curr.next
    return cnt 
print(count_sll(head))

# Searching in a linked list 
def search_sll(head,target):
    curr = head 
    while curr:
        if curr.data == target:
            return True
        curr = curr.next 
    return False
print(search_sll(head,15))

# INSERTION AT THE HEAD OF SLL 
def insertion_head_sll(head,val):
    new_node = Node(val)
    new_node.next = head 
    head = new_node 
    return head
head = insertion_head_sll(head,0)
traversal_sll(head)

# INSERTION AT THE END OF SLL 
def insertion_end_sll(head,val):
    new_node = Node(val)
    if head is None:
        return new_node
    curr = head 
    while curr.next:
        curr = curr.next 
    curr.next = new_node
    return head 
head = insertion_end_sll(head,30)
traversal_sll(head)

# DELETION AT THE HEAD OF SLL 
def deletion_head_sll(head):
    if head is None: 
        return None
    head = head.next
    return head 
head = deletion_head_sll(head)
traversal_sll(head)

# DELETION AT THE END OF SLL 
def deletion_end_sll(head):
    if head is None:
        return None
    if head.next is None:
        return None 
    curr = head 
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head
head = deletion_end_sll(head)
traversal_sll(head)
