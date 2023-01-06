# 290. Word Pattern

def wordPattern(pattern, s):
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    
    charToWord = {}
    wordToChar = {}
    for c,w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:
            return False
        if w in wordToChar and wordToChar[w] != c:
            return False
        charToWord[c] = w
        wordToChar[w] = c
    return True

pattern = "aaaa"
s = "dog dog dog dog"  
print(wordPattern(pattern, s))


# my attempt
# def wordPattern(pattern, s):
#     # create a word Array
#     wordArray = s.split()
    
#     if len(wordArray) != len(pattern):
#         return False
    
#     # map each character in the pattern to a word
#     dict = {}
#     for i in range(len(pattern)):
#         if not pattern[i] in dict.keys():
#             if not wordArray[i] in dict.values():
#                 dict[pattern[i]] = wordArray[i]
#             else:
#                 return False
#         else:
#             word = dict[pattern[i]]
#             if word != wordArray[i]:
#                 return False
            
#     return True
        

# Tricky edge case --> Two characters can not map to the same word : one character, one word
# illustration
# a -> cat
# b -> cat
# is wrong and should return false