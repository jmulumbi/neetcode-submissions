class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordsDict = {}

        for word in strs:
            sortedWords = sorted(word)
            finalWord = "".join(sortedWords)
    

            if finalWord in wordsDict:
                wordsDict[finalWord].append(word) 
            else:
                wordsDict[finalWord] = [word]
            
            
        return list(wordsDict.values())
