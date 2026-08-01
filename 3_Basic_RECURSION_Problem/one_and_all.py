## PRINT THE NAME 5 TIMES
def Name_5(n):
    if n==0:
        return
    print("AKSHAT")
    Name_5(n-1)

Name_5(5)

## Print linearly from 1 to N(forward revursive)
def Print_num(i,n):
    if i>n:
        return 
    print(i)
    Print_num(i+1,n)

Print_num(1,8)
                    

## Print linearly from 1 to N( Backtracking )
def Print_num(n):
    if n==0:
        return
    Print_num(n-1)                                     # 1->n
    print(n)                 

Print_num(8)

## Print lineraly from N to 1 (backtracking)
def Print_num(i , n):
    if i>n:
        return 
    Print_num(i+1,n)
    print(i)                                           # n->1
Print_num(1,8)

## Print linearly from N to 1 (forward recursive)
def Print_num(n):
    if n==0:
        return 
    print(n)
    Print_num(n-1)                                     # n->1
Print_num(8)


## Print the sum of n numbers (parametrized recursion)
def Print_sum(n, total):
    if n == 0:
        print(total)
        return
    Print_sum(n-1,total+n)

Print_sum(5,0)
    
## Print the sum of n numbers (functional recursion)
def Print_sum(n):
    if n==0:
        return 0
    return n+Print_sum(n-1)     
print(Print_sum(5))
    
## Print the factorial of n number (functional recursion)
def Print_fac(n):
    if n == 0:
        return 1
    return n*Print_fac(n-1)
print(Print_fac(5))

## Print the factorial of n number (parametrised recursion)
def Print_fac(n,fac):
    if n==0:
        print(fac)
        return 
    Print_fac(n-1, fac*n)
Print_fac(6,1)


## Reverse the items of a list
def rev_arr(arr,i):
    n = len(arr)
    if i>n//2:                                      # this is the base case that checks that if i>2 !! 
        return 
    arr[i],arr[n-i-1] = arr[n-i-1], arr[i]
    rev_arr(arr, i+1)
arr =[1,3,5,4,2]
rev_arr(arr,0)
print(arr)

## Check if a string is palindrome or not 
def Palindrome(s, i):
    n = len(s)

    if i>=n//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return Palindrome(s,i+1)

s = "malayalam"
print(Palindrome(s,0))

## Write a recursive program to print fibbonacci series of n
def Fibonacci(n,a,b):
    if n == 0:
        return
    print(a)
    return Fibonacci(n-1, b , a+b)
Fibonacci(7,0,1)
    



