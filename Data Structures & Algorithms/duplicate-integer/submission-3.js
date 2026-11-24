class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        var duplicates = new Set()
        for (var x = 0; x<= nums.length;x++){
            if (duplicates.has(nums[x])){
                return true
            } else {
                duplicates.add(nums[x])
            }
        }
        return false
    }
    }
