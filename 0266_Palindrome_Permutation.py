from collections import Counter

#---- Time: O(n)
#---- space: O(n)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_c = Counter(s)
        counter=0
        for i in s_c:
            counter += s_c[i]%2

        return counter <=1


# carerac
