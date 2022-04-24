class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        
        memo = {}
        def recur(index, who):
            
            if (index, who) not in memo:
                
                if index == n - 2:
                    return preSum[index + 2] if who else -preSum[index + 2]
                
                if who:
                    ans = max(recur(index + 1, who), recur(index + 1, not who) + preSum[index + 2])
                else:
                    ans = min(recur(index + 1, who), recur(index + 1, not who) - preSum[index + 2])

                memo[index, who] = ans
                
            return memo[index, who]
        
        return recur(0, True)