"""
1.Time complexity - O(N*logN)
- log2N --> gives use how many time we can divide a number by eg 2^x = 32 , gives 5, since we can divide 32 by 2 fives times
2.Space complexity - O(N)
"""
def countBitsBruteForce(n):
    result = []
    if n == 0:
        result.append(0)
        return result
        
    for i in range(n+1):
        currentNum = i
        count = 0
        if i == 0:
            result.append(0)
            continue
        else:
            while currentNum > 0:
                rem = currentNum % 2
                currentNum = currentNum / 2
                if rem == 1:
                    count += 1
        result.append(count)
        
    return result

print(countBitsBruteForce(2))

