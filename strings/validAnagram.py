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


def isAnagramUsingMap(s, t):
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


print(isAnagramUsingMap("anagram", "nagaram"))
