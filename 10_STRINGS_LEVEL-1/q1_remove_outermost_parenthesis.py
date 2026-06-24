## BRUTE FORCE - TC - o(n)-- worst case o(n^2), SC - o(n)
def remove_outermost_parenthesis_brute(s):
    ans = ""
    open = 0
    close = 0
    start = 0
    for i in range(len(s)):
        if s[i] == '(':
            open+=1
        elif s[i] == ')':
            close+=1
        if open==close:
            ans+=s[start+1:i]
            open = 0
            close = 0
            start = i+1
    return ans
s1 = "(()())(())"
s2 = "(()())(())(()(()))"

print(remove_outermost_parenthesis_brute("()()"))