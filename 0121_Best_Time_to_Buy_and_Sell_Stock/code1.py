class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)<2): return 0;
        ans = max(prices[1:])-prices[0]
        for i in range(1,len(prices)-1):
            if(prices[i] > prices[i+1]):
                continue
            elif(prices[i] < prices[i-1]):
                ans = max(ans, max(prices[i+1:]) - prices[i])             
        if(ans < 0): ans = 0;
        return ans