class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        n = len(stones)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
            
        
        memo = {}
        def recur(i, j):
            
            key = str(stones[i: j + 1])
            
            if key not in memo:
            
                if i > j:
                    return 0

                left = preSum[j + 1] - preSum[i + 1]
                right = preSum[j] - preSum[i]

                memo[key] = max(left - recur(i + 1, j), right - recur(i, j - 1))
                
            return memo[key]
        
        return recur(0, n - 1)