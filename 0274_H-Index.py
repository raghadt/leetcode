class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations = sorted(citations)
        
        citations[:] = citations[::-1]
        
        h=1
        for i in range(len(citations)):
            if h <= citations[i]:
                h+=1
                
            else:
                break
        return h-1