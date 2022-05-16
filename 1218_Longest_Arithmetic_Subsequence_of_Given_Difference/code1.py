class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        n = len(arr)
        ans = 0
        dp = collections.defaultdict(int)
        
        for i in range(n):
            num = arr[i]
            dp[num] = max(dp[num], dp[num - difference] + 1)
            ans = max(ans, dp[num])
            
        return ans