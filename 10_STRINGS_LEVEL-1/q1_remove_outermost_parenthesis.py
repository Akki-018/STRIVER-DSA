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

print(remove_outermost_parenthesis_brute(s1))


## OPTIMAL CODE- we check then add and +=1 for "(" and subtract -=1 and check and then add ")" in the ans with one varibale balance
def remove_outerm_par_opt(s):
    ans = []
    balance = 0
    for i in s:
        if i=="(": 
            if balance>0:
                ans.append("(")
            balance+=1
        elif i==")":
            balance-=1
            if balance>0:
                ans.append(")")
    return "".join(ans)
s2 = "(()())(())(()(()))"
print(remove_outerm_par_opt(s2))
