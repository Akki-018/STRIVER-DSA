## REVERSE WORD of a str
# BRUTE 
def reverse_word_str_brute(s):
    words = []
    i = 0 
    while i<len(s):
        while i<len(s) and s[i]==" ":
            i+=1
        if i==len(s):
            break
        curr = ""
        while i<len(s) and s[i] != " ":
            curr+=s[i]
            i+=1
        words.append(curr)
    return " ".join(words[::-1])
s = "the sky is blue"
print(reverse_word_str_brute(s))

## OPTIMAL CODE 
def rev_word_str_opt(s):
    return " ".join(s.split()[::-1])
print(rev_word_str_opt(s))
