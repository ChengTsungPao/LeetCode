class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        
        memo = {}
        def recur(index):
            
            if index not in memo:
            
                if index == n - 1:
                    return 0

                ans = -float("inf")
                for i in range(index + 1, n):
                    ans = max(ans, preSum[i + 1] - recur(i))

                memo[index] = ans if abs(ans) != float("inf") else 0
                
            return memo[index]
        
        return recur(0)