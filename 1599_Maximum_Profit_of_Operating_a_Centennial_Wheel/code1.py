class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        customers.reverse()
        
        ans = -1
        maxProfit = 0
        people = 0
        times = 0
        waiting = 0
        customer = 0
        
        while len(customers) > 0 or customer > 0:
            customer = (waiting + customers.pop()) if customers else waiting
            if customer >= 4:
                people += 4
                customer -= 4
            else:
                people += customer
                customer = 0
                
            times += 1
            profit = people * boardingCost - times * runningCost
            if profit > maxProfit:
                maxProfit = profit
                ans = times
                
            waiting = customer

        return ans