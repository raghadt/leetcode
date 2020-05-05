#-- this solutions uses Valley-peak.
#Time: O(n)
#Space: O(1)


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

    
print(max_profit)