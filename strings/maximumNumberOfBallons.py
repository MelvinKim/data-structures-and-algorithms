from typing import Counter


def maxNumberOfBalloons(text):
    if not text or len(text) < 7:
        return 0
    
    countText = Counter(text)
    balloon = Counter("balloon")
    
    res = len(text) # or float(inf)
    for c in balloon:
        res = min(res, countText[c] // balloon[c])
    return res
        
    


print(maxNumberOfBalloons("loonbalxballpoon"))