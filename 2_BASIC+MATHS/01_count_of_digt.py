## COUNTING OF A DIGIT IN A NUMBER 
#  Logical method
def Count_logical(n):
    cnt = 0
    while n>0:
        cnt+=1
        n//=10
    return cnt
n = 253
print(Count_logical(n))

#  Easy method
def Count_Easy(n):
    return len(str(n))
print(Count_Easy(n))

