class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create Hashmap to store value and index for number tracking
        hashmap = {}
        #Iterating through numbers to help naviagate through the nums array along with index
        for i,num in enumerate(nums):
            #Find the difference between target and current number
            complement = target - num #10 - 4 = 6
            #Checking to see whether the difference number is in the hashmap
            if complement in hashmap:
                #If it is return the index of the difference number, and the current number index 
                return [hashmap[complement], i]
            else:
                #If not store the number in the hashmap with the value which it has
                #Repeating loop and ensuring that the different numbers are added to the list
                hashmap[num] = i