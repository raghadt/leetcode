#-- Check if there's a repeating string
#-- return true or false
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s*2)[1:-1]