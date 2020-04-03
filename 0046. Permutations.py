#https://leetcode.com/problems/permutations/

"""
Using backtrack:
    19.44%
    Time: partial permutation

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first):
            if first==n:
                output.append(nums[:])
            
            for i in range(first,n):
                nums[first], nums[i] = nums[i],  nums[first]
                backtrack(first+1)
                nums[i],  nums[first] =   nums[first], nums[i] 
        
        n=len(nums)
        output=[]
        backtrack(0)
        return output



"""
Using DFS
56.72% 

""""

def permute(nums):

    res = []
    def dfs(nums,path):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
#             print("n={}, i={}".format(nums, i))
#             print("new n = {}".format(nums[:i]+nums[i+1:]))
#             print("path= {}".format(path))
#             print()
            dfs(nums[:i]+nums[i+1:], path+[nums[i]])
            
    dfs(nums,[])
    return res

nums=[1,2,3]
permute(nums)