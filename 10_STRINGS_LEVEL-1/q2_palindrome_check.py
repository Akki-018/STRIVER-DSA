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
def palindrome_str(x):
    return x == x[::-1]
print(palindrome_str("ab"))