class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        sell_0 = 0
        buy_1 = buy_2 = sell_1 = sell_2 = -float("inf")
        
        for price in prices:
            tmp_sell_0, tmp_sell_1 = sell_0, sell_1
            
            sell_1 = max(sell_1, buy_1 + price)
            sell_2 = max(sell_2, buy_2 + price)
            buy_1 = max(buy_1, tmp_sell_0 - price)
            buy_2 = max(buy_2, tmp_sell_1 - price)

        return max(sell_0, sell_1, sell_2, buy_1, buy_2)