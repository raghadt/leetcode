#--- Time: O(N+M)
#--- Space: O(N+M)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=[]
        for i in S:
            if i=='#' and len(s)!=0:
                s.pop()
            elif i!='#':
                s.append(i)
        s = "".join(s)

        t=[]
        for i in T:
            if i=='#' and len(t)!=0:
                t.pop()
            elif i!='#':
                t.append(i)
        t = "".join(t)
        
        return s==t