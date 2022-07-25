class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:        

        n = len(nums)
        
        dp = [[0] + [1] + [0] * (n - 1) for _ in range(n)]
        maxLengthDp = [1] * n
        maxLength = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLengthDp[i] = max(maxLengthDp[i], maxLengthDp[j] + 1)
                    maxLength = max(maxLength, maxLengthDp[i])
                    for k in range(1, n + 1):
                        dp[i][k] += dp[j][k - 1]
                        
        return sum([dp[i][maxLength] for i in range(n)])