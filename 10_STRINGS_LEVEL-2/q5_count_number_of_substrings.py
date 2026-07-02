## PROBLEM - 1 ==> Count the number of substrings of a string
def count_num_substr(s):
    return int((len(s)*(len(s)+1)/2))
print(count_num_substr("abcde"))

