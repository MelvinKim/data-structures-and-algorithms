class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return 0
        
        prefix = []
        postfix = []
        result = 1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            result *= nums[i - 1]
            prefix.append(result)
        prefix.insert(0, 1)
        print(prefix)
        
        result = 1
        for i in range(n - 1):
            result *= nums[i + 1]
            postfix.append(result)
        postfix.insert(n-1, 1)
        print(prefix)
        
        idx = 0
        for num1, num2 in zip(prefix, postfix):
            prefix[idx] = num1 * num2
            idx += 1
        
        return prefix
    
    
nums = [1,2,3,4]
solution = Solution()
print(solution.productExceptSelf(nums))