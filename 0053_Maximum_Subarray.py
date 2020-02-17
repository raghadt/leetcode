#https://leetcode.com/problems/maximum-subarray


# ------------- GREEDY APPROACH
# ---- 35%

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1,len(nums)):
            curr_sum = max(nums[i], curr_sum+nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum


# ------------ another approach %96

mxm = float("-inf")
cur = 0
for num in nums:
    print(cur)
    if cur < 0:
        cur = num
    else:
        cur += num

    if mxm < cur:
        mxm = cur