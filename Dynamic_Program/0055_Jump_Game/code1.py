class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        dp = n - 1 # 目前最小的合法位置
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= dp:
                dp = i
                
        return dp == 0
        