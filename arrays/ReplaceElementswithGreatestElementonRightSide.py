def replaceElementsBruteForce(arr):
    arr_copy = arr
    n = len(arr_copy)
    idx = 0
    for i in range(len(arr) - 1):
        maxNum = max(arr[i+1:])
        arr_copy[idx] = maxNum
        idx += 1
        
    arr_copy[n-1] = -1
    return arr_copy
    
def replaceElementsOptimal(arr):
    # reverse iteration
    rightMax = -1
    
    for i in range(len(arr) - 1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax
        
    return arr

nums = [17,18,5,4,6,1] 
print(replaceElementsOptimal(nums))