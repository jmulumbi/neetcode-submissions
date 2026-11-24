class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Checks to see if the length of s and t are the same. If not then they cannot be anagrams
        if len(s) != len(t):
            return False
        #Creates a dictionary to keep track of the values of the letters within the 
        frequencyDict = {

        }
        #For loop to iterate through each letter in s
        for letter in s:
            #If the letter is in the frequency dictionary give it a value of 1 
            if letter in frequencyDict:
                frequencyDict[letter] += 1
                #If it is not then give it an increment of one to its value 
            else:
                frequencyDict[letter] = 1
    #for loop to iterate through the letters in t 
        for letter in t:
            #If the letter is already in the frequencyDict then decrement its value by one 
            if letter in frequencyDict:
                frequencyDict[letter] -= 1
                #If the value gets less than zero then there is no way that they can be anagrams 
                #due to their lengths being different 
                if frequencyDict[letter] < 0:
                    return False
            else:
                return False
        
        for count in frequencyDict.values():
            if count != 0:
                return False
        return True 
        
