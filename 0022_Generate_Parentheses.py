class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left= "(" *n
        right = ")"*n
        ans=[]
        l=0
        r=0
        def back_track(s,l, r):
            if len(s)== (2*n):
                ans.append(s)
                return
            
            if l<n:
                back_track(s+'(', l+1, r)
            if r < l:
                
                back_track(s+')', l, r+1)
                
        back_track('',0,0)
        return ans