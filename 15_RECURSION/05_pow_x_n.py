## Return the x**n
def pow_x_n(x,n):
    if n<0:
        return 1/pow_x_n(x,-n)
    if n==0:
        return 1 
    half = pow_x_n(x,n//2)
    if n%2==0:
        return half*half
    else:
        return x*half*half
print(pow_x_n(2,10))


