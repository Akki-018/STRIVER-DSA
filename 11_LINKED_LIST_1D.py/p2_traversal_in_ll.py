## TRAVERSAL IN A SLL 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
head = n1
n1.next = n2
n2.next = n3 
n3.next = n4
def print_ll(head):
    current = head
    while current:
        print(current.data)
        current = current.next
print_ll(head)

def count_node_ll(head):
    current = head
    cnt=0
    while current:
        cnt+=1
        current = current.next
    return f"Number of nodes in the linked list: {cnt}" 
print(count_node_ll(head))








