class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A=="" and B=="":
            return True
        if len(A) != len(B):
            return False
#         if not B[0] in A:
#             return False
        
        return B in (A*2)