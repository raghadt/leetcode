#-- counter is o(n) so o(n)+o(n)=o(n)

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = collections.Counter(s)
        c_t = collections.Counter(t)
        
        return c_s == c_t