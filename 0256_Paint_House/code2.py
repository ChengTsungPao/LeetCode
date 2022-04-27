class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [0] * 3
        
        for cost in costs:
            newDp = [0] * 3
            
            newDp[0] = min(dp[1], dp[2]) + cost[0]
            newDp[1] = min(dp[0], dp[2]) + cost[1]
            newDp[2] = min(dp[0], dp[1]) + cost[2]
            
            dp = newDp

        return min(dp)