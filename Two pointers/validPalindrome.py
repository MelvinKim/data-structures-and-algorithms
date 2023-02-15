class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        
        s_lower = s.lower()
        print(s_lower)
        
        n = len(s_lower)
        left = 0
        right = n - 1
        while left < right:
            import pdb; pdb.set_trace()
            if s_lower[left] == " ":
                left += 1
            if s_lower[right] == " ":
                right -= 1
             
            import pdb; pdb.set_trace()
            if s_lower[left].isalnum():
                if s_lower[right].isalnum():
                    if s_lower[left] != s_lower[right]:
                        import pdb; pdb.set_trace()
                        return False
                right -= 1
            left += 1
            right -= 1
        
        return True
    
sol = Solution()
s = "race a car"
print(sol.isPalindrome(s))