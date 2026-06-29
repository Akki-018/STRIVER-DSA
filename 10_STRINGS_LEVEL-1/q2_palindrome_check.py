## CHECK if a number is palindrome or not 
def palindrome(x):
    temp = x
    rev = 0
    while temp>0:
        rev = rev*10+temp%10
        temp = temp//10
    return x == rev 
print(palindrome(1011))

## CHECK IF A string IS PALINDROME OR NOT 
#Direct method
def palindrome_str(x):
    return x == x[::-1]
print(palindrome_str("aba"))

#TWO POINTER APPROACH 
def palindrome_str_opt(x):
    low = 0 
    high = len(x)-1
    for i in range(len(x)):
        if x[low]!=x[high]:
            return False
        low+=1
        high-=1
    return True
print(palindrome_str_opt("abab"))


