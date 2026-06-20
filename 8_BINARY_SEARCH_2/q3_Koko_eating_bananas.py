import math
## PROBLEM STATEMENT 
# Return the minimum integer k such that Koko can eat all the bananas within h hours

## BRUTE FORCE SOLUTION -- TC - O(n*max(piles)),SC-0(1)
def minEatingSpeed(piles, h):
    for i in range(1,max(piles)+1):
        totalhrs = 0
        for j in piles:
            totalhrs+=math.ceil(j/i)
        if totalhrs<=h:
            return i
print(minEatingSpeed([3,6,7,11],8))

## OPTIMAL SOLUTION -- TC - O(n*log2(max(piles)))
def minEatingSpeed_opt(piles,h):
    def total(piles,d):
        totalhrs = 0
        for j in piles:
            totalhrs+=math.ceil(j/d)
        return totalhrs
    low = 1
    high = max(piles)
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2
        totalhrs = total(piles,mid)
        if totalhrs<=h:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
print(minEatingSpeed_opt([3,6,7,11],8))
            

        





