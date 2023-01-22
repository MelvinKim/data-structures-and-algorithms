"""
0(1) Time --> we are guaranteed that every input is going to be a 32-bit integer
0(1) Space
"""
def hammingWeightSolutionOne(n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res

"""
0(1) Time --> we are guaranteed that every input is going to be a 32-bit integer
0(1) Space
"""
def hammingWeightSolutionTwo(n):
    res = 0
    while n:
        n = n & (n-1)
        res += 1    
    return res


""" 
signed --> can take both positive and negative values
unsigned --> can not take a sign, only positives

NB:
1000000 - 1 = 0111111
"""