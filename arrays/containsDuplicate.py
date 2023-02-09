def containsDuplicate(nums):
    if nums == None:
        return False

    hashTable = {}
    for i in range(len(nums)):
        if nums[i] not in hashTable:
            hashTable[nums[i]] = 1
        else:
            return True
    return False

def containsDuplicateUsingHashset(nums):
    hashset = set()
    
    for n in nums:
        if n  in hashset:
            return True
        hashset.add(n)
        
    return False


print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
# use a map
# map each element with it's correspoding count value
# eg [1, 2,3,1] --> {1: 2, 2:1, 3:1}
# loop over the elements of the map, if at any time you find a count greater than 2, return false , else return true
