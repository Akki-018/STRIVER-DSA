## PRIME NUMBER 
def Prime(n):
    a = True
    for i in range(2,int(n**(1/2))):
        
        if n%i == 0 :
            a = False
            break
    return a == True
n = 12
print(Prime(n))



