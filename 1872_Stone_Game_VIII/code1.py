class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        
        memo = {}
        def recur(index, who):
            
            if (index, who) not in memo:
            
                if index == n - 1:
                    return 0

                if who:
                    ans = -float("inf")
                    for i in range(index + 1, n):
                        ans = max(ans, recur(i, not who) + preSum[i + 1])
                else:
                    ans = float("inf")
                    for i in range(index + 1, n):
                        ans = min(ans, recur(i, not who) - preSum[i + 1])  

                memo[index, who] = ans if abs(ans) != float("inf") else 0
                
            return memo[index, who]
        
        return recur(0, True)