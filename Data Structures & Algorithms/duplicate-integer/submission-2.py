class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
#Integer Array nums 
#If any array appears more than once, returns true 
#Else returns false

        duplicates = set()
        for num in nums:
            if num in duplicates:
                return True
            else:
                duplicates.add(num)
        return False


