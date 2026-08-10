## TO GENERATE ALL THE TYPES OF PARENTHESIS 
def gener_paren(n):
    ans = []
    def recursion(open,closed,string):
        if open==n and closed == n:
            ans.append(string)

        if open<n:
            recursion(open+1,closed,string+"(")
        if closed<open:
            recursion(open,closed+1,string+")")
    recursion(0,0,"")
    return ans 
print(gener_paren(3))