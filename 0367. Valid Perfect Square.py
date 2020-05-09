class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left=2
        right= num/2
        
        
        while left<=right:
            x = (left+right)//2
            guess = x*x
            
            if guess == num:
                return True
            
            elif guess > num:
                right = x-1
            else:
                left= x+1
                
        return Falsey