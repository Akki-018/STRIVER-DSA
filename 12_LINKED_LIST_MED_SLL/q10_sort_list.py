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

## OPTIMAL CODE - TC - o(nlogn),SC -o(1)
def sort_list_opt(head):
    if not head or not head.next:
        return head
    def mid_head(head):
        if not head or not head.next:
            return head 
        slow = head 
        fast = head
        prev = None 
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev 
    mid = mid_head(head)
    right = mid.next
    mid.next = None
    left = head 

    left_list = sort_list_opt(left)
    right_list = sort_list_opt(right)

    def merge_sort(left,right):
        dummy = Node(-1)
        tail = dummy
        curr1 = left
        curr2 = right
        while curr1 and curr2:
            if curr1.data<=curr2.data:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next 
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        return dummy.next 
    
    return merge_sort(left_list,right_list)
head = sort_list_opt(head)
traversal_sll(head)
        