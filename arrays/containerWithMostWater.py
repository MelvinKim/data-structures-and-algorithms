class Solution(object):
    def maxAreaBruteForce(self, heights):
        if not heights:
            return 0
        
        maxArea = 0
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
               currentArea = (r - l) * min(heights[l], heights[r])
               maxArea = max(maxArea, currentArea)
        return maxArea
    
    def maxAreaOptimal(self, heights):
        maxArea = 0
        l = 0
        r = len(heights) - 1
        
        while (l < r):
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, area)
            
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
                
        return maxArea
    

sol = Solution()
nums = [1,1]
print(sol.maxAreaOptimal(nums))