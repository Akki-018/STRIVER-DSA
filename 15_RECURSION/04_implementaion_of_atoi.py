## ATOI - ASCII to INTEGER 
# ex: -> "1234" to 1234 , "7" -> 7 , "0009" -> 9 
## atoi("1234") = atoi("123")*10+4
def rec_imp_atoi(s):
    if len(s)==0:
        return 0 
    small = rec_imp_atoi(s[:-1])
    last = int(s[-1])
    return small*10+last
s = "-234"
print(rec_imp_atoi(s))