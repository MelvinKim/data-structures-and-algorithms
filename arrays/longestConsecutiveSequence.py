""" 
Time complexity - O(N*log N) 
Space complexity - O(1) Space
"""
def longestConsecutiveUsingSorting(nums):
    if not nums:
        return 0
    
    nums.sort()
    
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
                
    return max(longest_streak, current_streak)

"""
Time complexity - O(N)
Sapce complexity - O(N)

- checking if an element doesn't have a left neighbour, if so that's the start of a sequence
- to get the length of a sequence, count how many numbers come after the elment which doesn't have a left neighbour
"""
def longestConsecutiveOptimalNeetCodeSolution(nums):
    numsSet = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in numsSet:
            length = 0
            while (n + length) in numsSet:
                length += 1
            longest = max(longest, length)
            
    return longest

def longestConsecutiveOptimalMySolution(nums):
    numsSet = set(nums)
    longestStreak = 0
    for n in nums:
        if n-1 in numsSet:
            continue
        
        currentNum = n
        currentStreak = 0
        while currentNum in numsSet:
            currentStreak += 1
            currentNum += 1
        longestStreak = max(longestStreak,currentStreak)
    return longestStreak

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutiveUsingSorting(nums))
print(longestConsecutiveOptimalNeetCodeSolution(nums))
print(longestConsecutiveOptimalMySolution(nums))
    