class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter= max_len = 0
        dic = {0:0}
        
        for index, val in enumerate(nums, 1):
            
            if val == 0:
                counter -=1
            else:
                counter+=1
            
            if counter in dic:
                max_len = max(max_len, index-dic[counter])
            else:
                dic[counter] = index
                
                
        return max_len