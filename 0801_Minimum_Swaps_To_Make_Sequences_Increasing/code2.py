class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        def swap(i, nums1, nums2):
            nums1[i], nums2[i] = nums2[i], nums1[i]
            
        def isValid(i):    
            return i - 1 < 0 or (nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i])  
        
        dp = [[float("inf")] * 2 for i in range(n + 1)]
        
        dp[n] = [0, 0]
        for i in range(n - 1, -1, -1):                
            for isSwap in [True, False]:
                if isSwap: i > 0 and swap(i - 1, nums1, nums2)
                
                # No swap
                if isValid(i): dp[i][isSwap] = dp[i + 1][False]
                # swap
                swap(i, nums1, nums2)
                if isValid(i): dp[i][isSwap] = min(dp[i][isSwap], dp[i + 1][True] + 1)
                swap(i, nums1, nums2)
                
                if isSwap: i > 0 and swap(i - 1, nums1, nums2)

        return dp[0][False]