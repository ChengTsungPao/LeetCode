class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                dp1[i] = dp1[i - 1] + 1
            if arr[~i] > arr[~i + 1]:
                dp2[~i] = dp2[~i + 1] + 1
        
        ans = 0
        for left, right in zip(dp1, dp2):
            if left > 1 and right > 1:
                ans = max(ans, left + right - 1)
                
        return ans