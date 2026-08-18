## Return all the letter combinations of a phone number from a string 
def combinations_phone(s):
    if not s:
        return []
    mapp = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    ans = []
    def recurse(i,str):
        if i==len(s):
            ans.append(str)
            return 
        word = mapp[s[i]]
        for j in word:
            recurse(i+1,str+j)
    recurse(0,"")
    return ans 
print(combinations_phone("23"))