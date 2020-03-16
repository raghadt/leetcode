#--------------- 5% lmao

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
            
        return -1





#------- 76$ using hashmap

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        c = Counter(s)
        
        for i, v in enumerate(s):
            if c[v]==1:
                return i
            
        return -1

        