# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

#-- 55%
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:len(nums1)]
        nums1.extend(nums2)
        nums1.sort()


#-- 95.77%

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # del nums1[m:len(nums1)]
        # nums1.extend(nums2)
        # nums1.sort()
        
        nums1[:] = sorted(nums1[:m] + nums2)