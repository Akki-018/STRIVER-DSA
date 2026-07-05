## RETURN THE LARGEST ODD NUMBER STRING IN A STRING 
# BRUTE FORCE -- TC - O(n^2)
def largest_odd_str_brute(num):
    if int(num)%2==1 :
        return num
    maxi = float('-inf')
    for i in range(len(num)):
        for j in range(i,len(num)):
            a = int(num[i:j+1])
            if a%2==1:
                maxi = max(maxi,a)
    if maxi == float('-inf'):
        return ""
    else:
        return str(maxi)
print(largest_odd_str_brute(str(24)))


## OPTIMAL SOLUTION 
def largest_odd_str_opt(num):
    for i in range(len(num)-1,-1,-1):
        if int(num[i])%2==1:
            return num[:i+1]
    return ""
print(largest_odd_str_opt(str(24352)))

 
