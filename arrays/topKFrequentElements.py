"""
Bucket sort
O(N) Time
- looping through the nums' values to store themm in a map,  O(N)
- looping through the storage array, from the back looking for top k frequent elements,  O(N)
O(N) + O(N) = O(2N) = O(N)
0(N) Size
- we will create an array of size (n) , n = length of the nums array
- we will have an array where the index represents the count, 
  and the element will be the values that occur that number of times
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]# [[], [], [], [], [], ....]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
solution = Solution()
nums = [1,1,1,2,2,2,2,2,8,8,8,4]
k = 3
print(solution.topKFrequent(nums, k))