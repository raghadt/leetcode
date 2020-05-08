class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        while len(stones)>1:
            stones = sorted(stones)
            if stones[-1]==stones[-2]:
                # print(stones[-2:])
                del stones[-2:]
            else:
                val =stones[-1]-stones[-2]
                del stones[-2:]
                stones.append(val)
            #print(stones)
        if len(stones)==0:
            return 0
        return stones[0]





#----------- Shorter solution:

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        while len(stones)>1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1-stone_2)
                
        return stones[0] if stones else 0
        