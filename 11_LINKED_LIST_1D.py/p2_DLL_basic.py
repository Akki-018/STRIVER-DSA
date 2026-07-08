## DOUBLY LINKED LIST - Every node contains two pointer - prev and next with the data of the node , we can go backwords, 
# CREATING A DLL 
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None 

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
head = n1
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4 
n4.prev = n3
n4.next = n5 
n5.prev = n4

# FORWARD TRAVERSAL 
def forward_traversal(head):
    curr = head 
    while curr:
        print(curr.data , end =" <-> ")
        curr = curr.next 
    print("None")
forward_traversal(head)

# BACKWARD TRAVERSAL 
def backward_traversal(head):
    if head is None:
        return None
    curr = head 
    while curr.next:
        curr = curr.next
    while curr:
        print(curr.data , end = " <-> ")
        curr = curr.prev
    print("None")
backward_traversal(head)

# Count the number of nodes 
def count_dll(head):
    curr = head 
    cnt = 0 
    while curr:
        cnt+=1
        curr = curr.next
    return cnt 
print(count_dll(head))

# Search the element in the dll 
def search_dll(head,target):
    curr = head 
    while curr:
        if curr.data == target:
            return True
        curr = curr.next
    return False
print(search_dll(head,40))

# INSERT AT THE HEAD OF A DLL 
def insert_head_dll(head,val):
    new_node = Node(val)
       
    new_node.next = head
    head.prev = new_node
    return new_node
head = insert_head_dll(head,0)
forward_traversal(head)

# INSERT AT THE END OF A DLL 
def insert_end_dll(head,val):
    new_node = Node(val)
    if head is None:
        return new_node
    curr = head 
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr 
    return head
head = insert_end_dll(head,60)
forward_traversal(head)

# DELETE THE HEAD OF A DLL 
def delete_head_dll(head):
    if not head:
        return None
    if not head.next:
        return head 
    head = head.next
    head.prev = None
    return head 
head = delete_head_dll(head)
forward_traversal(head)

# DELETE THE END OF A DLL 
def delete_end_dll(head):
    if not head:
        return None
    if not head.next:
        return None 
    curr = head 
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head
head = delete_end_dll(head)
forward_traversal(head)


