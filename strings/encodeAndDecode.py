class Solution:
    def encode(self, strs):
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    
    def decode(self,str):
        res = []
        i = 0
        while i < len(str):
            j  = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # tells how many characters we have to read after  "j"
            newWord = str[j + 1 : j + 1 + length]
            res.append(newWord)
            i = j + 1 + length # reset the "i" pointer
        
        return res
            
solution = Solution()
print(solution.encode(["i", "love", "code"]))
print(solution.decode(solution.encode(["i", "love", "code"])))




















# class Solution:
#     # encode
#     def encode(self, strs):
#         res = ""
#         for s in strs:
#             res += str(len(s)) + "#" + s
#         return res
        
#     # decode 
#     def decode (self, str):
#         res = []
#         i = 0
        
#         while i < len(str):
#             j = i
#             while str[j] != "#":
#                 j += 1
#             length = int(str[i:j])
#             res.append(str[j + 1 : j + 1 + length])
#             i = j + 1 + length
#         return res