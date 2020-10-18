#-- this solutions uses Valley-peak.
#Time: O(n)
#Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley= prices[0]
        peak = prices[0]
        max_profit = 0
        while i< len(prices)-1:
            print(i)
            while i<len(prices)-1 and prices[i]>=prices[i+1]:
                i+=1
            valley = prices[i]
            while(i < len(prices)-1 and prices[i]<=prices[i+1]):
                i+=1
            peak = prices[i]
            max_profit += peak - valley


        return (max_profit)


#--- same approach, but simple pass

class Solution:
    def maxProfit(self, price: List[int]) -> int:
        mx_profit = 0
        
        for i in range(1, len(price)):
            if price[i]> price[i-1]:
                mx_profit+= price[i] - price[i-1]
                
        return mx_profit