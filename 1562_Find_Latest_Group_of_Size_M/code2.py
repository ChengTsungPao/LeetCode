class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        n = len(arr)
        
        if n == m:
            return n
        
        ans = -1
        dp = [0] * (n + 2)
        
        for i, node in enumerate(arr):
            left_count = dp[node - 1]
            right_count = dp[node + 1]
            
            if left_count == m or right_count == m:
                ans = i
            
            dp[node - left_count] = dp[node + right_count] = left_count + right_count + 1
            
        return ans