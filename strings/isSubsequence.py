def isSubsequence(s, t):
    if not s:
        return True
    
    s_pointer = 0
    t_pointer = 0
    
    while(t_pointer < len(t)):
        if t[t_pointer] == s[s_pointer]:
            s_pointer += 1
            if s_pointer == len(s):
                return True
        else:
            t_pointer += 1
        
        
    return False


s = "ace"
t = "abcde"
print(isSubsequence(s, t))