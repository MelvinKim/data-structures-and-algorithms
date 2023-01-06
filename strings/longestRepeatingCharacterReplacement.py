def longestRepeatingCharacterReplacement(s, k):
    count = {}
    result = 0
    N = len(s)
    
    window_start = 0
    for window_end in range(N):
        count[s[window_end]] = 1 + count.get(s[window_end], 0)
        
        # check to ensure current window is valid
        while (window_end - window_start + 1) - max(count.values()) > k:
            # decrement count to character at the window start
            count[window_start] -= 1 
            window_start += 1
        
        result = max(result, window_end - window_start + 1)
        
    return result    


print(longestRepeatingCharacterReplacement("ABABBB", 2))