class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<10 :
        #     return True
        rev_st = str(x)
        # print(rev_st[::-1])
        return str(x)==rev_st[::-1]