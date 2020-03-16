#-- 89.31%

from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()
        
        paragraph_c = Counter(paragraph)
        
        ans=""
        best=0
        
        for i in paragraph_c:
            if paragraph_c[i] > best and i  not in banned_set:
                ans = i
                best = paragraph_c[i]
        return ans