class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:        
        
        # dp[i] => 0 ~ i包含i最長的increase sequence有幾個
        
        n = len(nums)
        dp = [0] * n
        maxLengthDp = [1] * n
        maxLength = 1
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLengthDp[i] = max(maxLengthDp[i], maxLengthDp[j] + 1)
                    maxLength = max(maxLength, maxLengthDp[i])

            if maxLengthDp[i] == 1:
                dp[i] = 1
            else:
                for j in range(i):
                    if nums[j] < nums[i] and maxLengthDp[i] == maxLengthDp[j] + 1:
                        dp[i] += dp[j]
                
        return sum([dp[i] if maxLengthDp[i] == maxLength else 0 for i in range(n)])