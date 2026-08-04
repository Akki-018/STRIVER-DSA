'''Recursion - A technique where a function calls itself to solve a smaller version of the same problem.
Every recursive function has three parts:
1. Base Case
   - Stops recursion.
2. Recursive Call
   - Calls the same function with a smaller input.
3. Self Work
   - Work performed by the current function.
Important:
Every recursive call must move towards the base case.
Otherwise, recursion never terminates.'''

##  BASIC PROBLEMS 
# Print the name 5 times 
def name(n):
   if n==0:
      return 
   print("Akshat")
   name(n-1)
name(5)

# Print linearly 1 to N (forward recursion)
def num_1(n,i):
   if i==n+1:
      return 
   print(i)
   num_1(n,i+1)
num_1(5,1)

# Print linearly N to 1 (backtracking)
def num_2(n):
   if n==0:
      return 
   print(n)
   num_2(n-1)
num_2(5)

# Print the sum of n numbers (parametrized recursion)
def sum_1(n,total):
   if n==0:
      print(total)
      return
   sum_1(n-1,total+n)
sum_1(5,0)

# Print the sum of n numbers (funcitonal recursion)
def sum_2(n):
   if n==0:
      return 0
   return n+sum_2(n-1)
print(sum_2(5))

# Print the factorial of n numbers(parametrized recursion)
def fact_1(n,total):
   if n==0:
      print(total)
      return 
   fact_1(n-1,total*n)
fact_1(4,1)

# Print the factorial of n numbers(functional recursion)
def fact_2(n):
   if n==0:
      return 1 
   return n*fact_2(n-1)
print(fact_2(5))

# Print fibonacci series of n 
def Fibonnacci(n,a,b):
   if n==0:
      return 
   print(a)
   return Fibonnacci(n-1,b,a+b)
Fibonnacci(6,0,1)
