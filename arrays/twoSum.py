def bruteForceTwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]


def twoSumUsingHashmap(nums, target):
    hashMap = {}  # val: index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:  # know we have a pair
            return [hashMap[diff], i]
        else:
            hashMap[n] = i


nums = [2, 7, 1, 1]
target = 9
print(twoSumUsingHashmap(nums, target))
