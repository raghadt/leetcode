"""
Time: O(N)
Space: O(1)

"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}
        result =0 
        n =len(s)
        for i in range(n):
                cur_char = s[n - 1 - i]
                result += alpha_map[cur_char]*(26**i)
        return result 