## GCD And LCM --
def GCD(n1,n2):
    while n2!=0:
        n1,n2 = n2,n1%n2
    return n1

def LCM(n1,n2):
    return int((n1*n2)/GCD(n1,n2))

n1 = 14
n2 = 7 
print(GCD(n1,n2))
print(LCM(n1,n2))
