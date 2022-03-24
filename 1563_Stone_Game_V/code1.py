class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        n = len(stoneValue)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stoneValue[i - 1]
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
            
                if i >= j:
                    return 0
            
                ret = 0
                for k in range(i, j):
                    left = preSum[k + 1] - preSum[i]
                    right = preSum[j + 1] - preSum[k + 1]

                    if left < right:
                        ret = max(ret, recur(i, k) + left)
                    elif left > right:
                        ret = max(ret, recur(k + 1, j) + right)
                    else:
                        ret = max(ret, recur(i, k) + left, recur(k + 1, j) + right)
                        
                memo[i, j] = ret
                    
            return memo[i, j]
        
        return recur(0, n - 1)   