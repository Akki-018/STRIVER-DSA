## At every position - we have exactly 2 choices
# GENERATE ALL BINARY STRINGS
def generate_all(n,i,s):
    if i==n:
        print(s)
        return
    generate_all(n,i+1,s+'0')
    generate_all(n,i+1,s+"1")
generate_all(2,0,"")

# GENERATE ALL BINARY STRINGS - without consecutive 1s
def generate_wihtout_1(n,i,s):
    if i==n:
        print(s)
        return 
    generate_wihtout_1(n,i+1,s+'0')
    if len(s) == 0 or s[-1]=="0":
        generate_wihtout_1(n,i+1,s+"1")
generate_wihtout_1(3,0,"")

# GENEARTE ALL BINARY STRINGS - without adjacent 0s
def generate_without_0(n,i,s):
    if i == n:
        print(s)
        return 
    if len(s)==0 or s[-1] == "1":
        generate_without_0(n,i+1,s+"0")
    generate_without_0(n,i+1,s+'1')
generate_without_0(3,0,"")


