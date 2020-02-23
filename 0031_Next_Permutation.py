class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums,reverse=True):
            nums[:]=sorted(nums)
            return
            

        # nums = [5,2,6,8,3]
        for i in range(len(nums)-1, 0, -1):
            # print(i)
            if nums[i]>nums[i-1]:
                j=i-1
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i]> nums[j]:
                nums[i], nums[j] = nums[j],nums[i]
                # print(nums)
                nums[j+1:]  = sorted(nums[j+1:])
                return
                