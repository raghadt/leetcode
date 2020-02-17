class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        p = prices
        mnm, curr = p[0], 0
        for i in range(1, len(p)):
            mnm = min(mnm, p[i])
            curr= max(curr, p[i] - mnm)
            
        return curr