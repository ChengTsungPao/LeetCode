class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @functools.lru_cache(None)
        def dp(idx):
            if idx >= n - 2:
                return 0
            return min([max(k - nums[idx + i], 0) + dp(idx + i + 1) for i in range(3)])
        return dp(0)