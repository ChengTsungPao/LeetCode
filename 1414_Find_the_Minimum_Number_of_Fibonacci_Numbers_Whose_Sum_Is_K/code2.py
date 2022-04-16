class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        dp = [1, 1]
        while dp[-1] + dp[-2] <= k:
            dp.append(dp[-1] + dp[-2])
        n = len(dp)

        ans = 0
        index = n
        while k > 0:
            index = bisect.bisect_right(dp, k, 0, index) - 1
            k -= dp[index]
            ans += 1
            
        return ans