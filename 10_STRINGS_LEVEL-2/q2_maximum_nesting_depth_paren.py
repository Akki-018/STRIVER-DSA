## We have to return the mximum depth of parenthesis in a string 
# we count the parenthess and return the maxium count 
def maximum_depth_parenthesis(s):
    cnt = 0 
    maxi = 0 
    for i in s:
        if i=='(':
            cnt+=1
            maxi = max(maxi,cnt)
        elif i==')':
            cnt-=1
    return maxi
s = "(1+(2*3)+((8)/4))+1"
print(maximum_depth_parenthesis(s))