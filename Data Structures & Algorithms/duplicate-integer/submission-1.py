class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearsTwice = []
        for num in nums:
            if num in appearsTwice:
                return True
            else:
                appearsTwice.append(num)
        return False 