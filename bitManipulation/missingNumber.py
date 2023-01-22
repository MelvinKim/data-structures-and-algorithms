"""
O(N^2) Time
O(1) Space
"""
def missingNumberBruteForce(nums):
    n = len(nums) + 1
    for i in range(n):
        if i not in nums:
            return i

"""
O(N) Time
O(1) Space

- Any number XOR by itself == 0
- XOR all the numbers in the array together and then also XOR by all the numbers that should be in the Array
"""
def missingNumberUsingXOR(nums):
    len_nums = len(nums)
    result = len_nums
    for i in range(len_nums):
        result ^= nums[i]
        result ^= i
        
    return result
   

"""
O(N) Time
O(1) Space

Downside 
- can lead to integer overflow when n is a very large number
"""
def missingNumberMathematicsFormula(nums):
    n = len(nums)
    expectedSum = (n * (n+1)) / 2  # Gaussian formula
    
    actualSum = 0 
    for i in nums:
        actualSum += i
        
    return expectedSum - actualSum


nums = [9,6,4,2,3,5,7,0,1]
print(missingNumberUsingXOR(nums))