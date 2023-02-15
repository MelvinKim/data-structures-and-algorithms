class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        maxLength = 1
        container = set()
        n = len(s)
        i = 0
        j = 1
        while j < n:
            if s[i] != s[j]:
                container.add(s[i])
                container.add(s[j])
                maxLength = max(maxLength, len(container))
                j += 1
            container.remove(s[i])
            i += 1
            j += 1
            
        return maxLength
    
    
sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))