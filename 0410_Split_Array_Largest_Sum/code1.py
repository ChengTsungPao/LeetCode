class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n+1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        
        memo = {}
        def recur(i, cut):
            
            if (i, cut) not in memo:
                
                if i >= n:
                    return float("inf")
                elif cut == 0:
                    return preSum[n] - preSum[i]

                ans = float("inf")
                for j in range(i + 1, n + 1):
                    ans = min(ans, max(preSum[j] - preSum[i], recur(j, cut - 1)))
                    
                memo[i, cut] = ans
                
            return memo[i, cut]
        
        return recur(0, m - 1)