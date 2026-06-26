## TO ROTATE THE STRING AND CHECK IF IT IS EQUAL TO THE given GOAL 
# BRUTE FORCE -- TC - O(n^2),SC - O(n)
def rotate_string_brute(str,goal):
    for i in range(len(str)):
        str = str[1:]+str[:1] # Keep rotating the array by one position till the length times 
        if str==goal:
            return True
    return False
str = "abcde"
goal = "cdeab"
print(rotate_string_brute(str,goal))

# OPTIMAL APPROACH - TC - O(1),SC- o(1)
def rotate_string_opt(str,goal):
    if goal in str+str:
        return True
    else:
        return False
str = "abcde"
goal = "cdeab"
print(rotate_string_opt(str,goal))
