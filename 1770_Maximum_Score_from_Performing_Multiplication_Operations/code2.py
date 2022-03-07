class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # 意義: dp[leftIndex][mulIndex] => leftIndex ~ rightIndex之間的最大score (rightIndex = -(mulIndex - leftIndex + 1))
        # 範圍: 0 <= leftIndex <= m && 0 <= mulIndex <= m

        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for mulIndex in range(m - 1, -1, -1):
            for leftIndex in range(mulIndex, -1, -1):
                rightIndex = -(mulIndex - leftIndex + 1)
                dp[leftIndex][mulIndex] = max(nums[leftIndex]  * multipliers[mulIndex] + dp[leftIndex + 1][mulIndex + 1], \
                                              nums[rightIndex] * multipliers[mulIndex] + dp[leftIndex + 0][mulIndex + 1])

        return dp[0][0]