## PALINDROME NUMBER -- If reverse of that num is equal to num
def isPalindrome(n):
    rev = 0
    dup = n
    while n>0:
        rev = rev*10 + n%10
        n = n//10
    return rev == dup
n = 121
print(isPalindrome(n))
n = 2324 
print(isPalindrome(n))
