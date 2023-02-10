""" 
O(n * log n) Time
O(1) Space
"""
def isAnagram(s, t):
    if s == None or t == None:
        return False
    if len(s) != len(t):
        return False

    # 1.sort
    s = sorted(s)
    t = sorted(t)
    # 2.compare
    if s == t:
        return True
    return False
"""
O(s + t) Time
s = length of s
t = length of t
O(s + t) Space
s = length of s
t = length of t
"""
def validAnagramNeetCodeSolution(s, t):
    if len(s) != len(t):
        return False
    
    countS = {}
    countT = {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # make sure the character counts are the same
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    
    return True

"""
O(s + t) Time
s = length of s
t = length of t
O(s + t) Space
s = length of s
t = length of t
"""
def isAnagramUsingMapMySolution(s, t):
    if s == None or t == None:
        return False
    if len(s) != len(t):
        return False

    dict_s = {}
    dict_t = {}
    for c in s:
        if c not in dict_s:
            dict_s["{}".format(c)] = 1
        else:
            dict_s["{}".format(c)] = dict_s["{}".format(c)] + 1
    for c in t:
        if c not in dict_t:
            dict_t["{}".format(c)] = 1
        else:
            dict_t["{}".format(c)] = dict_t["{}".format(c)] + 1
    # compare the two maps
    if dict_s != dict_t:
        return False
    return True


print(validAnagramNeetCodeSolution("anagram", "nagaram"))
