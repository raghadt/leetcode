#Time complexity : O(N) in the worst case when string lengths are close enough abs(ns - nt) <= 1, where N is a number of characters in the longest string. O(1) in the best case when abs(ns - nt) > 1.

#Space complexity : O(N) because strings are immutable in Python and Java and to create substring costs O(N) space.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        
        if ns > nt:
            return self.isOneEditDistance(t,s)
        
        if nt - ns > 1: #more than 1 edit
            return False
        
        for i in range(ns):
            if s[i]!= t[i]: #theres a differnece
                if ns==nt: #same length, nothing to worry about
                    return s[i+1:]==t[i+1:]
                else:
                    return s[i:] == t[i+1:] # bcuz t is longer than s
                
        return ns+1 == nt