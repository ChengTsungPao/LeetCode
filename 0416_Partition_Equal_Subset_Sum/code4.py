class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # 利用01背包問題的方法，將物品價值和重量都設為nums，找尋當背包重量為 sum(nums) // 2 是否能裝到價值為 sum(nums) // 2
        
        weight = sum(nums)
        if weight % 2 == 1:
            return False
        weight //= 2
        
        dp = [0] * (weight + 1)
        for i in range(1, len(nums) + 1):
            for w in range(weight, 0, -1):
                if w - nums[i - 1] >= 0:
                    dp[w] = max(dp[w], dp[w - nums[i - 1]] + nums[i - 1])
           
        return dp[-1] == weight
