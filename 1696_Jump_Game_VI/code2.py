class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        from sortedcontainers import SortedList
        
        n = len(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        
        bst = SortedList([(dp[0], 0)])
        
        for i in range(1, n):
            
            if i - k - 1 >= 0:
                bst.remove((dp[i - k - 1], i - k - 1))
                
            dp[i] = nums[i] + bst[-1][0]
            
            bst.add((dp[i], i))
            
        return dp[n - 1]