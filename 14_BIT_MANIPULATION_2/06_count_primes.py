## TO COUNT THE NUMBER OF PRIMES IN THE GIVEN RANGE 
# Brute force  - TC - O(n*(n**(1/2))) - usually TLE in leetcode 
def count_prime_brut(n):
    def Isprime(n):
        if n<2:
            return False
        i = 2 
        while i*i<=n:
            if n%i==0:
                return False 
            i+=1
        return True 
    cnt = 0 
    for i in range(2,n):
        if Isprime(i):
            cnt+=1
    return cnt 
print(count_prime_brut(10))

## OPTIMAL SOLUTION 
def count_prime_opt(n):
    if n<2:
        return 0 
    isprime = [True]*n
    isprime[0] = False
    isprime[1] = False
    for i in range(2,int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i,n,i):
                isprime[j] = False
    return sum(isprime)
print(count_prime_opt(10))


            