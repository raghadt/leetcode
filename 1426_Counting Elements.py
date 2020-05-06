
class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic = {i:0 for i in arr}
        
        for i in arr:
            if i+1 in dic.keys():
                dic[i+1]+=1
        
        return sum(dic.values())
                