## Return the x**n
def pow_x_n(x,n):
    if n==0:
        return 1 
    return pow_x_n(x,n//2)**pow_x_n(x,n//2)
print(pow_x_n(2,10))

