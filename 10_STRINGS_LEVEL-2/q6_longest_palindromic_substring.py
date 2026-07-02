## Return the longest palindromic substring in the given string if any 
# BRUTE FORCE - TC - O(n^3) , SC - O(n)
def longest_palindromic_substr_brute(s):
    ans = ""
    maxi = 0 
    for i in range(len(s)):
        for j in range(i,len(s)):
            a = s[i:j+1]
            if a==a[::-1]:
                if len(a)>maxi:
                    maxi = len(a)
                    ans = a 
    return ans 
s = "babad"
print(longest_palindromic_substr_brute(s))