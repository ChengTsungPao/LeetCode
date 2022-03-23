class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        
        n = len(nums)
        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)
        
        for index in range(1, n + 1):
            for s in dp[index - 1]:
                dp[index].add(s)
                dp[index].add(nums[index - 1] + s)
                
            if target in dp[index]:
                return True
            
        return False