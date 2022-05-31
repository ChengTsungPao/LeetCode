class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n+1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            
            
        dp = [[preSum[n] - preSum[i]] + [0] * (m - 1) for i in range(n)]       
        
        for i in range(n - 1, -1, -1):
            for cut in range(1, m):
                
                ans = float("inf")
                left = i + 1
                right = n - cut + 1
                
                while left < right:
                    mid = left + (right - left) // 2
                    
                    leftPartValue = preSum[mid] - preSum[i]
                    rightPartValue = dp[mid][cut - 1]
                    
                    ans = min(ans, max(leftPartValue, rightPartValue))
                    if leftPartValue <= rightPartValue:
                        left = mid + 1
                    else:
                        right = mid
                    
                dp[i][cut] = ans
                
        return dp[0][m - 1]