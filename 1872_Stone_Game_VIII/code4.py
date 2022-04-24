class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        
        memo = {}
        def recur(index):
            
            if index not in memo:
                
                if index == n - 2:
                    return preSum[index + 2]

                memo[index] = max(recur(index + 1), preSum[index + 2] - recur(index + 1))
                
            return memo[index]
        
        return recur(0)