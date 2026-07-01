## conver the string to integer 
# BRUTE FORCE - approach - we just check for the - , + , " " , and the numbers , and put cases on them 
def string_to_int(s):
    ans = ""
    i = 0 
    while i<len(s) and s[i]==" ":
        i+=1
    if i<len(s) and s[i] == "+" or s[i] == "-":
        ans+=s[i]
        i+=1
    while i<len(s) and s[i].isdigit():
        ans += s[i] 
        i+=1
    if ans =="" or ans == "+" or ans == "-":
        return 0
    num = int(ans)
    if num>2**31-1:
        return 2**31-1
    elif num<-2**31:
        return -2**31
    return num

s = " -042"
print(string_to_int(s))

# OPTIMAL CODE 
def string_to_int_opt(s):
    num = 0 
    sign = 1
    i = 0 
    while i<len(s) and s[i]==" ":
        i+=1
    if i<len(s) and (s[i]=="-" or s[i]=="+"):
        if s[i]=='-':
            sign = -1
        i+=1
    while i<len(s) and s[i].isdigit():
        digit = ord(s[i])-ord('0') 
        if num>(2**31-1)//10 or (num==(2**31-1)//10 and digit>7):
            return 2**31-1 if sign == 1 else -2**31
        num = num*10+digit
        i+=1
    return sign*num
s = " -042"
print(string_to_int_opt(s))

    