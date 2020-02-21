#---97.39% 

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")

        s = re.sub(r'[^A-Za-z0-9]', '', s)
        s=s.lower()
        
        if len(s)<=1:
            return True

        if len(s)<=2 and s[0]!=s[1] :
            return False

        
        return s==s[::-1]