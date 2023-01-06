def pivotIndexOptimal(nums):
    if not nums:
        return -1
    
    totalSum = 0
    leftSum = 0
    
    # calculate the totalSum
    for n in nums:
        totalSum += n
        
    for i in range(len(nums)):
        if totalSum - leftSum - nums[i] == leftSum:
            return i
        
        leftSum += nums[i]
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndexOptimal(nums))




""" 
# My intial bruteForec solution
def pivotIndexBruteForce(nums):
    if not nums:
        return -1
    
    sumLeft = 0
    sumRight = 0
    n = len(nums)
    for i in range(n):
        if i == 0:
            sumLeft = 0
        else:
            sumLeft = calculateSumToTheLeft(nums, i)
            
        if i == n-1:
            sumRight = 0
        else:
            sumRight = calculateSumToTheRight(nums, i, n)
            
        if sumLeft == sumRight:
            return i
        
    return -1

def calculateSumToTheLeft(nums, i):
    sum = 0
    for i in range(0, i):
        sum += nums[i]
        
    return sum

def calculateSumToTheRight(nums, i, n):
    sum = 0
    for i in range(i+1, n):
        sum += nums[i]
        
    return sum

"""
