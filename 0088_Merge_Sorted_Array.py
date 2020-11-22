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

#Time: O((n+m) log(n+m))
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # del nums1[m:len(nums1)]
        # nums1.extend(nums2)
        # nums1.sort()
        
        nums1[:] = sorted(nums1[:m] + nums2)


# 2 pointers approach

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Make a copy of nums1.
        nums1_copy = nums1[:m] 
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0 
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n: 
            if nums1_copy[p1] < nums2[p2]: 
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]