## SECOND LARGEST AND SECOND SMALLEST ELEMENT IN ARRAY 
def Second_order_element(arr):
    largest = second_largest = -float('inf')
    smallest = second_smallest = float('inf')
    for num in arr:
        # second largest
        if num>largest:
            second_largest = largest
            largest = num
        elif num<largest and num>second_largest:
            second_largest = num
        
        # second Smallest
        if num<smallest:
            second_largest = smallest
            smallest  = num
        elif num>smallest and num<second_smallest:
            second_smallest = num 

    return [second_smallest,second_largest]
arr = [5,2,3,6,7,1,12]
print(Second_order_element(arr))

