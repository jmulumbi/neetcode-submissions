class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        # for i,j in enumerate(s):
        #     if i in dictionary:
        #         j == 1
        #     else:
        #         j+=1
            
        # for x,y in dictionary:
        #     if x in dictionary:
        #         y -= 1
        #     else:
        #         y += 1
        
        freqDict = {}

        for letter in s:
            if letter in freqDict:
                freqDict[letter] += 1
            else:
                freqDict[letter] = 1

        for letter in t:
            if (letter not in freqDict) or (freqDict[letter] < 0):
                return False
            else:
                freqDict[letter] -= 1
        
        for letters in freqDict:
            if freqDict[letters] != 0:
                return False
        
        return True 
