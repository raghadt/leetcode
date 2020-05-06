# 1. using Prefix Sum 
#--49.59% 
# Time: O(n)
# Space O(1) -> s and left
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left=0
        
        for i in range(len(nums)):
            if left == (s-nums[i]):
                return i
            left+=nums[i]
            s-=nums[i]
            
        return -1


