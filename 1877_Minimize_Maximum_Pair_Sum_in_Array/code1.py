class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[~i])
            
        return ans