class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        n = len(stones)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
            
        
        memo = {}
        def recur(i, j, who):
            
            key = str(stones[i: j + 1]) + str(who)
            
            if key not in memo:
            
                if i > j:
                    return 0

                left = preSum[j + 1] - preSum[i + 1]
                right = preSum[j] - preSum[i]

                if who:
                    ans = max(recur(i + 1, j, not who) + left, recur(i, j - 1, not who) + right)

                else:
                    ans = min(recur(i + 1, j, not who) - left, recur(i, j - 1, not who) - right)
                    
                memo[key] = ans
                
            return memo[key]
        
        return recur(0, n - 1, True)