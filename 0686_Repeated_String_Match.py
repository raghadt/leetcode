class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(set(B) - set(A)) > 0:
            return -1
        
        s=""
        for i in range(len(B)):
            s+=A
            if s.find(B)!=-1:
                return i+1
            if len(s)> len(A)+len(B):
                return -1
        return -1