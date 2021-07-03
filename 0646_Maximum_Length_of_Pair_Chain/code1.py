class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        ans, dp = 1, {len(pairs) - 1: 1}
        for i in range(len(pairs) - 2, -1, -1):
            dp[i] = 0
            for j in range(i + 1, len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans