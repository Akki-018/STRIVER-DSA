## Palindromes - checking by recursion
# For a string 
def palindrome_str(s,left,right):
    if left>=right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome_str(s,left+1,right-1)
s = "madams"
print(palindrome_str(s,0,5))

#