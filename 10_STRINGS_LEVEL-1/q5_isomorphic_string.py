## REturn True if all the charac of both the stings map to each other , otherwise False 
def isomorphic_string(s,t):
    map_st = {}
    map_ts = {}
    for i in range(len(s)):
        if s[i] in map_st:
            if map_st[s[i]] != t[i]:
                return False
        elif t[i] in map_ts:
            if map_ts[t[i]] != s[i]:
                return False
        else:
            map_st[s[i]] = t[i]
            map_ts[t[i]] = s[i]
    return True
s = "paper"
t = "title"
print(isomorphic_string(s,t))