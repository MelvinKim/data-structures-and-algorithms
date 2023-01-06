def findDisappearedNumbersBruteForce(nums):
    if not nums:
        return []
    
    min = 1
    max = len(nums)
    result = []
    
    for i  in range(min, max+1):
        if i not in nums:
            result.append(i)
            
    return result

nums = [2,2]
print(findDisappearedNumbersBruteForce(nums))