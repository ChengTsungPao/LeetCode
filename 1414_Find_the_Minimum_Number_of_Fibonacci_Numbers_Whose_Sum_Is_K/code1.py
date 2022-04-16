class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        dp = [1, 1]
        while dp[-1] + dp[-2] <= k:
            dp.append(dp[-1] + dp[-2])
        n = len(dp)

        ans = float("inf")
        def recur(k, index, step):
            nonlocal ans
            
            if k == 0:
                ans = min(ans, step)
                return True
            elif k < 0:
                return

            for i in range(index, -1, -1):
                if recur(k - dp[i], i, step + 1):
                    return True
                
        recur(k, n - 1, 0)
        return ans