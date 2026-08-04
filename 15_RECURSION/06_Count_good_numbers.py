## TO COUNT THE GOOD NUMBERS
# GOOD NUMBERS - if the digits at even indices are even digits, and at odd indices are prime digits"
def cnt_good_num(n):
    mod = 10**9+7
    even = (n+1)//2
    odd = n//2
    def pow(x,n):
        if n==0:
            return 1 
        half = pow(x,n//2)
        if n%2==0:
            return (half*half)%mod
        else:
            return (x*half*half)%mod
    ans = pow(5,even)*pow(4,odd)
    return ans%mod
print(cnt_good_num(50))

