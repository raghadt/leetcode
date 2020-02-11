class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #  s = ''.join(map(str, numList))
    
        digits = ''.join(map(str, digits))
        plus_one = int(digits) + 1
        plus_one = str(plus_one)
        plus_one_list=[]
        for i in plus_one:
            plus_one_list.append(int(i))
        return (plus_one_list)