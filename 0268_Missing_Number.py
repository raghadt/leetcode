#55.35% 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        dic={}
        dic = { i : 0 for i in range(len(nums)+1) }

        for i in nums:
            dic[i]+=1

        for k, v in dic.items():
            if v==0:
                return (k)


#-- 55.11% lol

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sum_v = 0
        sumv = [i for i in range(len(nums)+1)]

        return sum(sumv)-sum(nums)




# ---- using gasuuan sum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return (len(nums)*(len(nums)+1))//2 - sum(nums)