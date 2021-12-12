class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:  
        '''
        dp[step][start] => 從start走到dst，最多走step步，所需之花費
        
        Init:
            dp[0][start] => flights
            
        Method:
            dp[step][start] = min(dp[step - 1][start], cost[start, mid] + dp[step - 1][mid] ... ) -> mid = 1 ~ n - 1
        '''
            
        dp = [[float("inf")] * n  for _ in range(k + 1)]
        
        cost = {}
        dp[0][dst] = 0
        for start, end, price in flights:
            cost[start, end] = price
            if end == dst:
                dp[0][start] = min(dp[0][start], price)
        
        for step in range(1, k + 1):
            for start in range(n):
                dp[step][start] = dp[step - 1][start]
                for mid in range(n):
                    dp[step][start] = min(dp[step][start], cost.get((start, mid), float("inf")) + dp[step - 1][mid])   

        return dp[k][src] if dp[k][src] != float("inf") else -1