# a really bad solution lol
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(-1)
        max_ones = 0
        current_ones = 0
        
        for i in range(len(nums)):
            if nums[i]==1:
                current_ones +=1
            else:
                max_ones = max(max_ones, current_ones)
                current_ones=0
                
        return max_ones

def findMaxConsecutiveOnes(self, nums):
    #1. split the str by zero
    #2.  
  return max(map(len, ''.join(map(str, nums)).split('0')))