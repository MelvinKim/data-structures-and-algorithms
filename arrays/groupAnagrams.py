class Solution(object):
    def groupAnagrams(self, strs):
        result = []
        hashMap = {}
        if strs == None:
            return result

        for s in strs:
            sortedArr = sorted(s)
            sortedStr = "".join(sortedArr)
            if sortedStr in hashMap:
                hashMap[sortedStr].append(s)
            else:
                hashMap[sortedStr] = []
                hashMap[sortedStr].append(s)

        for key, val in hashMap.items():
            result.append(val)

        return result