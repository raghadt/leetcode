#--- using linear search
"""
79.43% 
Time: O(N)
Space: O(1)
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max(nums)

        for i in nums:
             if i != max1:
                if i*2 > max1:
                    return -1

        return nums.index(max1)