#-------- 77%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums[:] = sorted(nums)
        return len(nums)