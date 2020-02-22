# -- Time: O(n)
#-- space: O(1)
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        def check(x): #A[0] or B[0]
            rotate_a=0
            rotate_b=0
            
            for i in range(len(A)):
                if x!=A[i] and x!=B[i]:
                    return -1
                
                if x!=A[i]:
                    rotate_a +=1
                elif x!=B[i]:
                    rotate_b+=1
    
            
            return min(rotate_a, rotate_b)
        
        rotations = check(A[0])
        
        if rotations != -1 or A[0]==B[0]:
            return rotations
        
        else:
            return check(B[0])