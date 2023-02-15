class Solution(object):
    def threeSumBruteForce(self, nums):
        n = len(nums) - 1
        res = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    nums1 = nums[i]
                    nums2 = nums[j]
                    nums3 = nums[k]
                    sub_result = []
                    if nums1 + nums2 + nums3 == 0:
                        sub_result.append([nums1, nums2, nums3])
                        res.append(sub_result)
                            
        return res
    
sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSumBruteForce(nums))