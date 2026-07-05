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

# OPTIMAL CODE 
def longest_palind_substr_opt(s):
    def expand(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    start = 0
    end = 0 
    for i in range(len(s)):
        odd = expand(i,i)
        even = expand(i,i+1)
        length = max(odd,even)
        if length>end-start+1:
            start = i-(length-1)//2
            end = i+length//2
    return s[start:end+1]
s = "babad"
print(longest_palind_substr_opt(s))
