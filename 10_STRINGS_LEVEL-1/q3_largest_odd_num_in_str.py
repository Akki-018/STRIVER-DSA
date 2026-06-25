## RETURN THE LARGEST ODD NUMBER STRING IN A STRING 
# BRUTE FORCE -- TC - O(n^2)
def largest_odd_str(num):
    if int(num)%2==1 :
        return num
    maxi = float('-inf')
    for i in range(len(num)):
        for j in range(i,len(num)):
            a = int(num[i:j+1])
            if a%2==1:
                if a>maxi:
                    maxi = a
    if maxi == float('-inf'):
        return ""
    else:
        return str(maxi)
print(largest_odd_str(str(24)))
 
